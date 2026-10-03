import json
import logging
import threading
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from .resume_data import get_resume

logger = logging.getLogger(__name__)

SPLINE_SCENE_URL = "https://prod.spline.design/kZDDjO5HuC9GJUM2/scene.splinecode"


def landing(request):
    lang = request.GET.get("lang") or request.COOKIES.get("lang") or "fa"
    if lang not in ("fa", "en"):
        lang = "fa"
    context = {
        "lang": lang,
        "dir": "rtl" if lang == "fa" else "ltr",
        "spline_scene_url": SPLINE_SCENE_URL,
    }
    response = render(request, "main/landing.html", context)
    response.set_cookie("lang", lang, max_age=60 * 60 * 24 * 365, samesite="Lax")
    return response


def _send_notification_email(contact_message_id, name, phone, description):
    """Runs in a background thread — a slow/hung SMTP connection can never
    block or crash the actual web request anymore."""
    try:
        body = (
            f"نام: {name}\n"
            f"شماره تماس: {phone}\n"
            f"توضیحات: {description or '-'}"
        )
        send_mail(
            subject="کار",
            message=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
            fail_silently=False,
        )
    except Exception:
        # هر خطایی (تایم‌اوت، لاگین اشتباه، هر چیزی) فقط توی لاگ ثبت می‌شه،
        # چون این تابع توی یه ترد جدا اجرا می‌شه و هیچ‌وقت نباید کاربر رو تحت تأثیر قرار بده.
        logger.exception("Contact form notification email failed to send (message id=%s)", contact_message_id)


def _notify_by_email(contact_message):
    if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
        return
    thread = threading.Thread(
        target=_send_notification_email,
        args=(contact_message.id, contact_message.name, contact_message.phone, contact_message.description),
        daemon=True,
    )
    thread.start()


def resume(request):
    lang = request.GET.get("lang") or request.COOKIES.get("lang") or "fa"
    if lang not in ("fa", "en"):
        lang = "fa"

    sent = request.GET.get("sent") == "1"

    if request.method == "POST":
        form = ContactForm(request.POST, lang=lang)
        if form.is_valid():
            contact_message = form.save()
            _notify_by_email(contact_message)
            # Redirect-after-POST (Post/Redirect/Get): a page refresh after
            # this won't resubmit the form or double-save the message.
            redirect_response = redirect(f"{reverse('main:resume')}?lang={lang}&sent=1#contact")
            redirect_response.set_cookie("lang", lang, max_age=60 * 60 * 24 * 365, samesite="Lax")
            return redirect_response
    else:
        form = ContactForm(lang=lang)

    data = get_resume(lang)
    context = {
        "lang": lang,
        "dir": data["dir"],
        "other_lang": "en" if lang == "fa" else "fa",
        "r": data,
        "skills_json": json.dumps(data["skills_flat"]),
        "form": form,
        "sent": sent,
    }
    response = render(request, "main/resume.html", context)
    response.set_cookie("lang", lang, max_age=60 * 60 * 24 * 365, samesite="Lax")
    return response
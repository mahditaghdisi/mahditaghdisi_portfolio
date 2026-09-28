import json
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from .resume_data import get_resume

SPLINE_SCENE_URL = "https://prod.spline.design/kZDDjO5HuC9GJUM2/scene.splinecode"


def landing(request):
    context = {
        "spline_scene_url": SPLINE_SCENE_URL,
    }
    return render(request, "main/landing.html", context)


def _notify_by_email(contact_message):
    """Best-effort email notification — never breaks the page if email isn't configured."""
    if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
        return
    body = (
        f"نام: {contact_message.name}\n"
        f"شماره تماس: {contact_message.phone}\n"
        f"توضیحات: {contact_message.description or '-'}"
    )
    send_mail(
        subject="کار",
        message=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
        fail_silently=True,
    )


def resume(request):
    lang = request.GET.get("lang") or request.COOKIES.get("lang") or "fa"
    if lang not in ("fa", "en"):
        lang = "fa"

    sent = False
    if request.method == "POST":
        form = ContactForm(request.POST, lang=lang)
        if form.is_valid():
            contact_message = form.save()
            _notify_by_email(contact_message)
            sent = True
            form = ContactForm(lang=lang)
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
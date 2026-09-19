import json
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


def resume(request):
    lang = request.GET.get("lang") or request.COOKIES.get("lang") or "fa"
    if lang not in ("fa", "en"):
        lang = "fa"

    sent = False
    if request.method == "POST":
        form = ContactForm(request.POST, lang=lang)
        if form.is_valid():
            form.save()
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
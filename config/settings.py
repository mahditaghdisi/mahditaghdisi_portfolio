import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "insecure-dev-key-change-me")
DEBUG = os.environ.get("DEBUG", "True") == "True"

ALLOWED_HOSTS = [h.strip() for h in os.environ.get(
    "ALLOWED_HOSTS", "127.0.0.1,localhost"
).split(",") if h.strip()]

CSRF_TRUSTED_ORIGINS = [o.strip() for o in os.environ.get(
    "CSRF_TRUSTED_ORIGINS", ""
).split(",") if o.strip()]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        conn_health_checks=True,  # قبل از استفاده‌ی دوباره از یه کانکشن قدیمی، سالم‌بودنش رو چک می‌کنه
        # مهمه برای Neon: چون کامپیوتش بعد از چند دقیقه بی‌کاری می‌خوابه و بیدار می‌شه،
        # بدون این گزینه ممکنه جنگو بخواد از یه کانکشن "مرده" دوباره استفاده کنه و خطا بگیره.
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "main" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# سخت‌گیری‌های امنیتی — فقط وقتی DEBUG=False (یعنی روی Render) فعال می‌شن،
# تا موقع توسعه‌ی لوکال (http://127.0.0.1) مشکلی پیش نیاد.
if not DEBUG:
    SECURE_SSL_REDIRECT = True          # هر درخواست http رو خودکار به https ریدایرکت می‌کنه
    SESSION_COOKIE_SECURE = True        # کوکی سشن فقط روی https ارسال می‌شه
    CSRF_COOKIE_SECURE = True           # کوکی CSRF هم همینطور
    SECURE_HSTS_SECONDS = 31536000      # به مرورگر می‌گه یک سال فقط https رو قبول کنه
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True  # جلوی حدس نوع فایل توسط مرورگر رو می‌گیره
    X_FRAME_OPTIONS = "DENY"            # سایت داخل iframe سایت دیگه لود نشه (ضد clickjacking)

# ایمیل: اختیاریه — اگه EMAIL_HOST_USER / EMAIL_HOST_PASSWORD ست نشن،
# سایت بدون خطا کار می‌کنه، فقط ایمیل نوتیفیکیشن فرم تماس ارسال نمی‌شه.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", "587"))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_TIMEOUT = 10  # اگه Gmail توی ۱۰ ثانیه جواب نده، به جای گیرکردن بی‌نهایت، خطا می‌ده و رها می‌کنه
CONTACT_NOTIFY_EMAIL = os.environ.get("CONTACT_NOTIFY_EMAIL", "mahditaghdisi650@gmail.com")

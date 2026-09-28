# سایت شخصی مهدی تقدیسی (mahditaghdisi.ir)

پروژه‌ی جنگو برای لندینگ + رزومه‌ی دوزبانه (فارسی/انگلیسی).

## ساختار

- `config/` — تنظیمات پروژه جنگو
- `main/` — اپ اصلی
  - `views.py`, `urls.py`, `models.py`, `forms.py`, `admin.py`
  - `resume_data.py` — محتوای دوزبانه رزومه (برگرفته از رزومه‌ی ارسالی)
  - `templates/main/` — `base.html`, `landing.html`, `resume.html`
  - `static/main/` — `css/style.css` و فایل‌های JS (کرسر، تم، زبان، کره مهارت‌ها)

## اجرای لوکال

```bash
python -m venv venv
source venv/bin/activate      # ویندوز: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env           # مقادیر رو پر کن (SECRET_KEY حتماً عوض بشه)
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

سایت روی `http://127.0.0.1:8000` بالا میاد. `/admin/` هم پنل مدیریت پیام‌های فرم تماسه.

## دیپلوی روی Render

1. پروژه رو به یه ریپوی GitHub پوش کن.
2. توی Render یه **New > Blueprint** بساز و ریپو رو انتخاب کن (فایل `render.yaml` خودش سرویس وب + دیتابیس Postgres رو می‌سازه).
   - یا دستی: **New > Web Service**، ریپو رو وصل کن، Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`، Start Command: `gunicorn config.wsgi:application`.
3. یه **PostgreSQL** جدا هم بساز (اگه از Blueprint استفاده نکردی) و متغیر `DATABASE_URL` رو از داخلش کپی کن.
4. متغیرهای محیطی (Environment) رو ست کن: `SECRET_KEY` (یه مقدار تصادفی طولانی)، `DEBUG=False`، `ALLOWED_HOSTS=mahditaghdisi.ir,www.mahditaghdisi.ir,<your-app>.onrender.com`، `CSRF_TRUSTED_ORIGINS=https://mahditaghdisi.ir,https://www.mahditaghdisi.ir`، `DATABASE_URL`.
5. بعد از اولین دیپلوی موفق: `python manage.py migrate` و `python manage.py createsuperuser` رو از تب **Shell** توی Render اجرا کن.

## وصل کردن دامنه (ایرنیک + Cloudflare + Render)

1. توی Render، قسمت **Settings > Custom Domains** دامنه `mahditaghdisi.ir` و `www.mahditaghdisi.ir` رو اضافه کن؛ Render یه آدرس مقصد (CNAME) بهت میده.
2. وارد پنل Cloudflare شو، دامنه رو Add Site کن، و Nameserverهایی که Cloudflare میده رو توی پنل ایرنیک جایگزین Nameserverهای فعلی کن (معمولاً ۱ تا ۲۴ ساعت طول می‌کشه تا پراپاگیت بشه).
3. توی DNS پنل Cloudflare:
   - یه رکورد `CNAME` برای `www` به آدرسی که Render داد.
   - برای ریشه دامنه (`mahditaghdisi.ir`) از قابلیت `CNAME flattening` کلادفلر استفاده کن (رکورد CNAME روی ریشه هم می‌ذاری، کلادفلر خودش هندل می‌کنه) یا از رکورد A که Render مشخص کرده.
   - ابر نارنجی (Proxy) رو روشن نگه دار تا SSL/CDN رایگان کلادفلر فعال باشه.
4. توی تنظیمات SSL کلادفلر، حالت `Full` یا `Full (strict)` رو انتخاب کن.
5. بعد از پراپاگیت شدن DNS، سایت با HTTPS روی دامنه بالا میاد.

## نکات مهم

- کد کره‌ی مهارت‌ها یک "Tag Sphere" خالص با CSS 3D + JS هست (بدون نیاز به WebGL/کتابخانه‌ی جدا)، چون globe سبک magicui بر پایه نقشه‌ی دنیاست و برای نمایش متن مناسب نبود.
- افکت Border-beam با CSS خالص (`conic-gradient` + `@property`) پیاده شده، دقیقاً همون افکتی که خواسته بودی.
- کرسر سفارشی با رنگ وابسته به تم (روشن/تاریک) پیاده شده تا همیشه خوانا بمونه؛ روی موبایل/لمسی به‌صورت خودکار غیرفعال می‌شه.
- سین اسپلاین فعلی (`SPLINE_SCENE_URL` در `main/views.py`) یه صحنه‌ی نمونه‌ی عمومیه که ربات سرش با موس حرکت می‌کنه. اگه خودت صحنه‌ی اسپلاین اختصاصی داری، فقط کافیه لینک `.splinecode` رو جایگزین کنی.
- زبان صفحه‌ی لندینگ کاملاً سمت کلاینت (JS) سوییچ می‌شه و در `localStorage` ذخیره می‌مونه؛ صفحه‌ی رزومه کاملاً سمت سرور رندر می‌شه بر اساس `?lang=fa` یا `?lang=en` (و در سشن هم ذخیره می‌شه).

## ویژگی‌های جدید (نسخه‌ی magicui-inspired)

- **بیم‌های متحرک بین مهارت‌ها**: هر مهارت با مهارت کناری‌اش (بر اساس ترتیب حلقه‌ای) با یه خط انیمیشنی وصله. کره خودش دست‌نخورده مونده.
- **پاپ‌آپ موفقیت فرم تماس**: به‌جای پیغام سبز، یه مودال با دکمه OK باز می‌شه.
- **ایمیل نوتیفیکیشن (اختیاری)**: با پر شدن فرم، اگه `EMAIL_HOST_USER`/`EMAIL_HOST_PASSWORD` رو توی Environment ست کرده باشی، یه ایمیل با عنوان «کار» به `mahditaghdisi650@gmail.com` می‌ره. اگه ست نکنی، هیچ خطایی نمی‌ده، فقط ایمیل نمی‌فرسته. راهنمای ساخت App Password جیمیل توی `.env.example` هست.
- **کارت‌های سوابق/پروژه‌ها**: عنوانشون با اسکرول، حرف‌به‌حرف و رنگی reveal می‌شه (شبیه DiaTextReveal).
- **آیکون لینک روی کارت‌ها**: برای هر آیتم توی سوابق شغلی، پروژه‌ها، گواهینامه‌ها و فعالیت‌های داوطلبانه، اگه توی `main/resume_data.py` یه کلید `"image": "main/img/اسم-فایل.jpg"` بهش اضافه کنی، یه آیکون لینک پایین-چپ کارت ظاهر می‌شه که با کلیک، عکس رو توی یه پاپ‌آپ نشون می‌ده. فایل عکس رو باید بذاری توی `main/static/main/img/`. پیش‌فرض هیچ آیتمی عکس نداره (چون فایل نداشتم)، خودت هر جا خواستی اضافه کن.
- **Dock پایین صفحه**: آیکون خانه، رزومه و ایمیل، با افکت بزرگ‌نمایی هنگام هاور (شبیه دستگاه macOS dock).
- **دکمه ارسال پیام**: افکت پالس/ریپل با رنگ‌های خود سایت (نارنجی) نه رنگ آبی نمونه‌ی magicui.
- **نوار پیشرفت اسکرول**: بالای صفحه، هنگام اسکرول پر می‌شه.
- **عنوان بخش‌ها**: با ورود به دید (اسکرول)، با افکت blur-in ظاهر می‌شن.

هیچ‌کدوم از این‌ها نیاز به سرویس پولی Render نداره — همه‌چیز Vanilla JS/CSS داخل همون پروژه‌ست، فقط ایمیل نیاز به یه App Password رایگان جیمیل داره.

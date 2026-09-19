# -*- coding: utf-8 -*-
"""Static bilingual resume content, sourced from Mahdi's resume document."""

RESUME = {
    "fa": {
        "dir": "rtl",
        "name": "مهدی تقدیسی هادی‌پور",
        "title": "محقق هوش مصنوعی و بینایی کامپیوتر",
        "email": "mahditaghdisi650@gmail.com",
        "phone": "+98 915 693 7195",
        "location": "مشهد، خراسان رضوی",
        "linkedin": "LinkedIn",
        "summary_label": "خلاصه رزومه",
        "summary": (
            "محقق هوش مصنوعی، برنامه‌نویس و مدرس خودآموخته با سابقه توسعه پروژه‌های عملی "
            "در یادگیری عمیق و بینایی کامپیوتر (تشخیص چهره، تشخیص حرکت با شبکه‌های عمیق) و "
            "بیش از دو سال سابقه تدریس پایتون و ICDL در موسسات مختلف. علاقه‌مند به ادامه "
            "تحصیل و فعالیت پژوهشی در حوزه هوش مصنوعی."
        ),
        "skills_label": "مهارت‌ها",
        "skills_groups": [
            {"title": "زبان‌های برنامه‌نویسی", "items": ["Python", "C++", "C", "JavaScript"]},
            {"title": "یادگیری ماشین و عمیق", "items": ["Neural Networks", "OpenCV", "Computer Vision"]},
            {"title": "فریم‌ورک و ابزار", "items": ["Django", "PyQt6", "FastAPI"]},
            {"title": "پایگاه داده", "items": ["PostgreSQL", "MySQL"]},
            {"title": "سایر", "items": ["ESP32", "ICDL", "HTML", "CSS"]},
        ],
        "skills_flat": [
            "Python", "C++", "C", "JavaScript", "Django", "FastAPI", "PyQt6",
            "OpenCV", "Computer Vision", "Neural Networks", "PostgreSQL",
            "MySQL", "ESP32", "HTML", "CSS", "ICDL",
        ],
        "experience_label": "سوابق شغلی",
        "experience": [
            {"role": "محقق هوش مصنوعی و عضو تیم لیبلینگ", "org": "آپان — مشهد", "period": "اردیبهشت ۱۴۰۵ – مرداد ۱۴۰۵"},
            {"role": "کارشناس تست نرم‌افزار و اداری", "org": "آپان — مشهد", "period": "اردیبهشت ۱۴۰۵ – مرداد ۱۴۰۵"},
            {"role": "مدرس پایتون و هوش مصنوعی", "org": "آموزشگاه منوری — مشهد", "period": "اردیبهشت ۱۴۰۵ – اکنون"},
            {"role": "مدرس پایتون", "org": "آموزشگاه ذهن پویا — مشهد", "period": "اردیبهشت ۱۴۰۵ – اکنون"},
            {"role": "استاد حل تمرین (TA)", "org": "دانشگاه صنعتی سجاد — مشهد", "period": "بهمن ۱۴۰۲ – بهمن ۱۴۰۴"},
            {"role": "مدرس پایتون", "org": "دبیرستان بعثت — مشهد", "period": "مهر ۱۴۰۳ – بهمن ۱۴۰۳"},
            {"role": "مدرس پایتون", "org": "پایتون‌تیک — مشهد", "period": "خرداد ۱۴۰۳ – خرداد ۱۴۰۴"},
        ],
        "projects_label": "پروژه‌ها",
        "projects": [
            {
                "title": "تشخیص احساسات چهره انسان با YOLOv8",
                "desc": "پیاده‌سازی و fine-tune مدل YOLOv8 برای تشخیص احساسات چهره انسان.",
                "meta": "کارفرما: خویش‌فرما",
            },
            {
                "title": "توسعه فول‌استک وبسایت شخصی (پورتفولیو)",
                "desc": "توسعه فول‌استک وبسایت شخصی برای کارفرما با استفاده از جنگو برای بک‌اند.",
                "meta": "مرداد ۱۴۰۵ / شهریور ۱۴۰۵ — کارفرما: کارگاه بهروز صنعت",
            },
            {
                "title": "توسعه فول‌استک وبسایت فروشگاهی",
                "desc": "توسعه فول‌استک وبسایت فروشگاهی با استفاده از جنگو برای بک‌اند.",
                "meta": "مرداد ۱۴۰۵ / شهریور ۱۴۰۵",
            },
            {
                "title": "تشخیص بلادرنگ حرکت انسان (LRCN)",
                "desc": "ترجمه مقاله Long-term Recurrent Convolutional Network و پیاده‌سازی هوشمند آن برای تشخیص بلادرنگ حرکات انسان با شبکه‌های عمیق در پایتون.",
                "meta": "مهر ۱۴۰۴ — کارفرما: دانشگاه سجاد",
            },
            {
                "title": "پروژه گلخانه هوشمند",
                "desc": "پیاده‌سازی سیستم محلی گلخانه هوشمند با ارسال داده از طریق وای‌فای، با استفاده از میکروکنترلر ESP32.",
                "meta": "مهر ۱۴۰۴ — کارفرما: دانشگاه سجاد",
            },
            {
                "title": "ماشین‌حساب و برنامه یادداشت مشابه ویندوز ۱۰",
                "desc": "پیاده‌سازی ماشین‌حساب و نرم‌افزار یادداشت مشابه ویندوز ۱۰ با استفاده از کتابخانه PyQt6.",
                "meta": "مرداد ۱۴۰۳ / مهر ۱۴۰۴ — کارفرما: خویش‌فرما",
            },
        ],
        "education_label": "سوابق تحصیلی",
        "education": [
            {"degree": "کارشناسی مهندسی کامپیوتر", "org": "دانشگاه صنعتی سجاد — مشهد", "period": "بهمن ۱۴۰۰ – بهمن ۱۴۰۴"},
        ],
        "certificates_label": "دوره‌ها و گواهینامه‌ها",
        "certificates": [
            "مدرک فنی‌حرفه‌ای پایتون — آموزشگاه فنی‌حرفه‌ای مشهد",
            "Python Programming Fundamentals with Practical Examples — Faradars.org",
            "API Development with FastAPI Fundamentals in Python — Faradars.org",
            "Messenger App Development with Django Channels — Faradars.org",
            "Android Programming with Python and Kivy Framework — Faradars.org",
            "ICDL Seven Skills Fundamentals — Faradars.org",
            "SoloLearn: Python (Introduction, Intermediate, Developer), Introduction to C, SQL (Introduction, Intermediate)",
        ],
        "volunteer_label": "فعالیت‌های داوطلبانه",
        "volunteer": [
            {
                "title": "عضو کمیته علمی",
                "desc": "بررسی مقالات علمی در سمینار هوش مصنوعی و علوم انسانی، با همکاری دکتر جواد حمیدزاده و دانشکده علوم انسانی دانشگاه سجاد.",
                "period": "اردیبهشت ۱۴۰۴",
            },
            {
                "title": "کادر فنی مسابقه Capture The Flag (CTF)",
                "desc": "همکاری با دکتر محمدمهدی سالخورده حقیقی، دانشگاه سجاد و تیم افتا.",
                "period": "اردیبهشت ۱۴۰۴",
            },
            {
                "title": "کادر فنی مسابقه Space6 (ICPC)",
                "desc": "همکاری با دکتر امیرفرید امینیان‌مدرس، دانشگاه سجاد.",
                "period": "۱۷–۱۸ آبان ۱۴۰۳",
            },
        ],
        "references_label": "معرف‌ها",
        "references": [
            {"name": "دکتر حمیده احمدی", "role": "استاد دانشگاه سجاد مشهد، دانشکده صنایع"},
            {"name": "دکتر وحیده منعمی‌زاده", "role": "استاد دانشگاه سجاد مشهد، دانشکده کامپیوتر"},
        ],
        "contact_label": "ارتباط با من",
        "contact_desc": "برای همکاری، پروژه یا سوال، فرم زیر رو پر کن تا هر چه زودتر باهات تماس بگیرم.",
        "contact_success": "پیام شما با موفقیت ارسال شد. ممنون که باهام تماس گرفتید!",
        "contact_submit": "ارسال پیام",
        "back_home": "بازگشت به صفحه اصلی",
    },
    "en": {
        "dir": "ltr",
        "name": "Mahdi Taghdisi Hadipour",
        "title": "AI Researcher & Computer Vision",
        "email": "mahditaghdisi650@gmail.com",
        "phone": "+98 915 693 7195",
        "location": "Mashhad, Khorasan Razavi, Iran",
        "linkedin": "LinkedIn",
        "summary_label": "Summary",
        "summary": (
            "Self-taught AI researcher, developer, and instructor with hands-on experience "
            "building deep learning and computer vision projects (facial emotion recognition, "
            "human action recognition with deep networks), plus over two years teaching Python "
            "and ICDL at various institutes. Interested in pursuing graduate studies and research "
            "in artificial intelligence."
        ),
        "skills_label": "Skills",
        "skills_groups": [
            {"title": "Programming Languages", "items": ["Python", "C++", "C", "JavaScript"]},
            {"title": "Machine & Deep Learning", "items": ["Neural Networks", "OpenCV", "Computer Vision"]},
            {"title": "Frameworks & Tools", "items": ["Django", "PyQt6", "FastAPI"]},
            {"title": "Databases", "items": ["PostgreSQL", "MySQL"]},
            {"title": "Other", "items": ["ESP32", "ICDL", "HTML", "CSS"]},
        ],
        "skills_flat": [
            "Python", "C++", "C", "JavaScript", "Django", "FastAPI", "PyQt6",
            "OpenCV", "Computer Vision", "Neural Networks", "PostgreSQL",
            "MySQL", "ESP32", "HTML", "CSS", "ICDL",
        ],
        "experience_label": "Work Experience",
        "experience": [
            {"role": "AI Researcher & Labeling Team Member", "org": "Apan — Mashhad", "period": "May 2026 – Aug 2026"},
            {"role": "Software Test & Admin Specialist", "org": "Apan — Mashhad", "period": "May 2026 – Aug 2026"},
            {"role": "Python & AI Instructor", "org": "Monavvari Institute — Mashhad", "period": "May 2026 – Present"},
            {"role": "Python Instructor", "org": "Zehn-e-Pooya Institute — Mashhad", "period": "May 2026 – Present"},
            {"role": "Teaching Assistant (TA)", "org": "Sadjad University of Technology — Mashhad", "period": "Feb 2024 – Feb 2026"},
            {"role": "Python Instructor", "org": "Besat High School — Mashhad", "period": "Oct 2024 – Feb 2025"},
            {"role": "Python Instructor", "org": "PythonTik — Mashhad", "period": "Jun 2024 – Jun 2025"},
        ],
        "projects_label": "Projects",
        "projects": [
            {
                "title": "Human Facial Emotion Recognition with YOLOv8",
                "desc": "Implemented and fine-tuned a YOLOv8 model for human facial emotion recognition.",
                "meta": "Client: Self-employed",
            },
            {
                "title": "Full-Stack Personal Portfolio Website",
                "desc": "Built a full-stack personal portfolio website for a client using Django on the backend.",
                "meta": "Aug/Sep 2026 — Client: Behrooz Sanat Workshop",
            },
            {
                "title": "Full-Stack E-commerce Website",
                "desc": "Built a full-stack e-commerce website using Django on the backend.",
                "meta": "Aug/Sep 2026",
            },
            {
                "title": "Real-Time Human Action Recognition (LRCN)",
                "desc": "Translated the Long-term Recurrent Convolutional Network paper and implemented it in Python for real-time human action recognition with deep networks.",
                "meta": "Oct 2025 — Client: Sadjad University",
            },
            {
                "title": "Smart Greenhouse Project",
                "desc": "Built a local smart greenhouse system with Wi-Fi data transmission using an ESP32 microcontroller.",
                "meta": "Oct 2025 — Client: Sadjad University",
            },
            {
                "title": "Windows 10-style Calculator & Notes App",
                "desc": "Built a calculator and notes application resembling Windows 10's, using the PyQt6 library.",
                "meta": "Aug 2024 / Oct 2025 — Client: Self-employed",
            },
        ],
        "education_label": "Education",
        "education": [
            {"degree": "B.Sc. in Computer Engineering", "org": "Sadjad University of Technology — Mashhad", "period": "Feb 2022 – Feb 2026"},
        ],
        "certificates_label": "Courses & Certificates",
        "certificates": [
            "Python Technical & Vocational Certificate — Mashhad Technical & Vocational Training Center",
            "Python Programming Fundamentals with Practical Examples — Faradars.org",
            "API Development with FastAPI Fundamentals in Python — Faradars.org",
            "Messenger App Development with Django Channels — Faradars.org",
            "Android Programming with Python and Kivy Framework — Faradars.org",
            "ICDL Seven Skills Fundamentals — Faradars.org",
            "SoloLearn: Python (Introduction, Intermediate, Developer), Introduction to C, SQL (Introduction, Intermediate)",
        ],
        "volunteer_label": "Volunteer Activities",
        "volunteer": [
            {
                "title": "Scientific Committee Member",
                "desc": "Reviewed papers for the AI & Humanities seminar, organized with Dr. Javad Hamidzadeh and the Faculty of Humanities, Sadjad University.",
                "period": "May 2025",
            },
            {
                "title": "Technical Crew — Capture The Flag (CTF)",
                "desc": "Collaborated with Dr. Mohammad Mahdi Salkhordeh Haghighi, Sadjad University & Afta Team.",
                "period": "May 2025",
            },
            {
                "title": "Technical Crew — Space6 (ICPC)",
                "desc": "Collaborated with Dr. Amirfarid Aminian-Modarres, Sadjad University.",
                "period": "Nov 7–8, 2024",
            },
        ],
        "references_label": "References",
        "references": [
            {"name": "Dr. Hamideh Ahmadi", "role": "Professor, Sadjad University of Technology — Faculty of Industrial Engineering"},
            {"name": "Dr. Vahideh Monemizadeh", "role": "Professor, Sadjad University of Technology — Faculty of Computer Engineering"},
        ],
        "contact_label": "Get in Touch",
        "contact_desc": "For collaboration, project inquiries, or questions, fill out the form below and I'll get back to you soon.",
        "contact_success": "Your message was sent successfully. Thanks for reaching out!",
        "contact_submit": "Send Message",
        "back_home": "Back to Home",
    },
}


def get_resume(lang):
    return RESUME.get(lang, RESUME["fa"])

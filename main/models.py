from django.db import models


class ContactMessage(models.Model):
    name = models.CharField("نام", max_length=150)
    phone = models.CharField("شماره تماس", max_length=30)
    description = models.TextField("توضیحات پروژه", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"

    def __str__(self):
        return f"{self.name} — {self.phone}"

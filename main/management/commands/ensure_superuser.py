import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Creates (or updates the password of) a superuser from environment
    variables, without needing an interactive shell. Safe to run on every
    single deploy — if the user already exists it just updates the password
    and never crashes the build.

    Reads: DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL,
    DJANGO_SUPERUSER_PASSWORD
    """

    help = "Create or update the admin superuser from env vars (no shell needed)."

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            self.stdout.write(self.style.WARNING(
                "DJANGO_SUPERUSER_USERNAME/PASSWORD not set — skipping admin user creation."
            ))
            return

        User = get_user_model()
        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email, "is_staff": True, "is_superuser": True},
        )
        user.email = email or user.email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f"Created admin user '{username}'."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Admin user '{username}' already existed — password refreshed."))

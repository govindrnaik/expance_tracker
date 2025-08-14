from django.contrib.auth.models import User
from django.db import models


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    google_sheet_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Settings for {self.user.username}"

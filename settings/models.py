from django.db import models
from django.contrib.auth.models import User

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    google_sheet_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Settings for {self.user.username}"

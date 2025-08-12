from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from .forms import UserSettingsForm
from .models import UserSettings


class SettingsView(LoginRequiredMixin, View):
    template_name = "settings/settings.html"

    def get(self, request, *args, **kwargs):
        user_settings, created = UserSettings.objects.get_or_create(user=request.user)
        form = UserSettingsForm(instance=user_settings)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        user_settings, created = UserSettings.objects.get_or_create(user=request.user)
        form = UserSettingsForm(request.POST, instance=user_settings)
        if form.is_valid():
            form.save()
            return redirect("settings:settings")
        return render(request, self.template_name, {"form": form})

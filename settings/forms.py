from django import forms
from .models import UserSettings

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['google_sheet_url']
        widgets = {
            'google_sheet_url': forms.URLInput(attrs={'class': 'form-control'})
        }

# d:\govind_data\playground\expance_tracker\income\forms.py
from django import forms
from .models import Income, Source

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source', 'amount', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['source'].queryset = Source.objects.filter(user=user)

class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['name']
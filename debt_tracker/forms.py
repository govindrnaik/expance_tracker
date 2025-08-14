from django import forms

from .models import Debt, Payment


class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = ["name", "total_amount", "interest_rate", "due_date"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["amount", "date"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }

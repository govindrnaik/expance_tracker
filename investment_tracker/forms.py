from django import forms

from expenses.models import PaymentMethod

from .models import Investment, InvestmentType, Platform


class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class InvestmentTypeForm(forms.ModelForm):
    class Meta:
        model = InvestmentType
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = [
            "date",
            "investment_type",
            "platform",
            "amount",
            "description",
            "payment_method",
        ]
        widgets = {
            "date": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
            "investment_type": forms.Select(attrs={"class": "form-select"}),
            "platform": forms.Select(attrs={"class": "form-select"}),
            "payment_method": forms.Select(attrs={"class": "form-select"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(InvestmentForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["investment_type"].queryset = InvestmentType.objects.filter(
                user=user
            )
            self.fields["platform"].queryset = Platform.objects.filter(user=user)
            self.fields["payment_method"].queryset = PaymentMethod.objects.filter(
                user=user
            )
        self.fields["investment_type"].empty_label = "Select an investment type"
        self.fields["platform"].empty_label = "Select a platform"
        self.fields["payment_method"].empty_label = "Select a payment method"

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from expenses.models import PaymentMethod


class Platform(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ("user", "name")

    def __str__(self):
        return self.name


class InvestmentType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ("user", "name")

    def __str__(self):
        return self.name


class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    investment_type = models.ForeignKey(InvestmentType, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} - {self.investment_type.name} - {self.amount}"

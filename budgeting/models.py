from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from expenses.models import Category


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    month = models.PositiveIntegerField()
    year = models.PositiveIntegerField()

    class Meta:
        unique_together = ("user", "category", "year", "month")

    def __str__(self):
        return f"{self.category.name} ({self.year}-{self.month:02d})"

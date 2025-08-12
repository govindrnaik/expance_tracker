import random
from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from budgeting.models import Budget
from expenses.models import Category, Expense, PaymentMethod
from investment_tracker.models import Investment, InvestmentType, Platform


class Command(BaseCommand):
    help = "Adds dummy expenses to the database for a specific user."

    def add_arguments(self, parser):
        parser.add_argument(
            "username", type=str, help="The username of the user to add expenses for."
        )
        parser.add_argument(
            "count", type=int, help="The number of dummy expenses to create."
        )
        parser.add_argument(
            "--investments",
            type=int,
            default=5,
            help="The number of dummy investments to create.",
        )

    def handle(self, *args, **kwargs):
        username = kwargs["username"]
        count = kwargs["count"]
        investment_count = kwargs["investments"]

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING(f'User "{username}" does not exist.'))
            return

        # Get or create categories
        categories_names = [
            "Food",
            "Transport",
            "Utilities",
            "Entertainment",
            "Health",
            "Shopping",
            "Other",
        ]
        categories = [
            Category.objects.get_or_create(user=user, name=name)[0]
            for name in categories_names
        ]

        # Get or create payment methods
        payment_method_names = ["Cash", "Credit Card", "Debit Card", "Online"]
        payment_methods = [
            PaymentMethod.objects.get_or_create(user=user, name=name)[0]
            for name in payment_method_names
        ]

        # Get or create investment platforms
        platform_names = ["StockBrokerage", "CryptoExchange", "RealEstatePlatform"]
        platforms = [
            Platform.objects.get_or_create(user=user, name=name)[0]
            for name in platform_names
        ]

        # Get or create investment types
        investment_type_names = ["Stocks", "Bonds", "Crypto", "Real Estate"]
        investment_types = [
            InvestmentType.objects.get_or_create(user=user, name=name)[0]
            for name in investment_type_names
        ]

        # Create dummy budgets for the current month
        now = timezone.now()
        for category in categories:
            budget, created = Budget.objects.get_or_create(
                user=user,
                category=category,
                year=now.year,
                month=now.month,
                defaults={"amount": round(random.uniform(200.0, 1000.0), 2)},
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created budget: {budget}")
                )

        for i in range(count):
            category = random.choice(categories)
            payment_method = random.choice(payment_methods)
            expense = Expense.objects.create(
                user=user,
                date=timezone.now() - timedelta(days=random.randint(0, 28)),
                category=category,
                sub_category=f"Sub for {category.name}",
                amount=round(random.uniform(5.0, 200.0), 2),
                description=f"Dummy expense entry {i + 1}",
                payment_mode=payment_method,
            )
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created expense: {expense}")
            )

        for i in range(investment_count):
            investment = Investment.objects.create(
                user=user,
                date=timezone.now() - timedelta(days=random.randint(0, 365)),
                investment_type=random.choice(investment_types),
                platform=random.choice(platforms),
                amount=round(random.uniform(500.0, 5000.0), 2),
                description=f"Dummy investment entry {i + 1}",
                payment_method=random.choice(payment_methods),
            )
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created investment: {investment}")
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully added {count} dummy expenses for user "{username}".'
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully added {investment_count} dummy investments for user "{username}".'
            )
        )

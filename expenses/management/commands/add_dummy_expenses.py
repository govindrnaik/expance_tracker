import random
from datetime import date, timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from expenses.models import Expense


class Command(BaseCommand):
    help = "Adds dummy expenses to the database for a specific user."

    def add_arguments(self, parser):
        parser.add_argument(
            "username", type=str, help="The username of the user to add expenses for."
        )
        parser.add_argument(
            "count", type=int, help="The number of dummy expenses to create."
        )

    def handle(self, *args, **kwargs):
        username = kwargs["username"]
        count = kwargs["count"]

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User "{username}" does not exist.'))
            return

        categories = [
            "Food",
            "Transport",
            "Utilities",
            "Entertainment",
            "Health",
            "Shopping",
            "Other",
        ]

        for i in range(count):
            expense = Expense.objects.create(
                user=user,
                date=date.today() - timedelta(days=random.randint(0, 365)),
                category=random.choice(categories),
                amount=round(random.uniform(5.0, 200.0), 2),
                description=f"Dummy expense entry {i + 1}",
            )
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created expense: {expense}")
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully added {count} dummy expenses for user "{username}".'
            )
        )

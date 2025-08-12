import random
from datetime import date, timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from income.models import Income, Source


class Command(BaseCommand):
    help = "Creates dummy income data for testing purposes."

    def handle(self, *args, **options):
        # Get the first user or create one if none exist
        user, created = User.objects.get_or_create(username="admin")
        if created:
            user.set_password("password")
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created user: {user.username}")
            )

        # Dummy data for sources
        source_names = [
            "Salary",
            "Freelance",
            "Investment",
            "Gift",
            "Bonus",
            "Rental Income",
        ]

        # Create sources for the user
        sources = []
        for name in source_names:
            source, _ = Source.objects.get_or_create(user=user, name=name)
            sources.append(source)

        self.stdout.write(self.style.SUCCESS(f"Created/found {len(sources)} sources."))

        # Create dummy income entries
        for _ in range(20):  # Create 20 dummy income entries
            source = random.choice(sources)
            amount = round(random.uniform(500, 5000), 2)
            days_ago = random.randint(0, 365)
            income_date = date.today() - timedelta(days=days_ago)
            description = f"Dummy income for {source.name}"

            Income.objects.create(
                user=user,
                source=source,
                amount=amount,
                date=income_date,
                description=description,
            )

        self.stdout.write(
            self.style.SUCCESS("Successfully created 20 dummy income entries.")
        )

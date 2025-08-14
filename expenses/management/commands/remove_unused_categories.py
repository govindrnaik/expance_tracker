from django.core.management.base import BaseCommand

from expenses.models import Category, Expense


class Command(BaseCommand):
    help = "Removes categories that are not associated with any expenses."

    def handle(self, *args, **options):
        self.stdout.write("Checking for unused categories...")
        unused_categories = 0
        for category in Category.objects.all():
            if not Expense.objects.filter(category=category).exists():
                self.stdout.write(f"Deleting unused category: {category.name}")
                category.delete()
                unused_categories += 1

        if unused_categories == 0:
            self.stdout.write(self.style.SUCCESS("No unused categories found."))
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully removed {unused_categories} unused categories."
                )
            )

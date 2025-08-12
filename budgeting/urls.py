from django.urls import path

from .views import (
    BudgetCreateView,
    BudgetDeleteView,
    BudgetListView,
    BudgetUpdateView,
)

app_name = "budgeting"

urlpatterns = [
    path("", BudgetListView.as_view(), name="budget_list"),
    path("create/", BudgetCreateView.as_view(), name="budget_create"),
    path("<int:pk>/update/", BudgetUpdateView.as_view(), name="budget_update"),
    path("<int:pk>/delete/", BudgetDeleteView.as_view(), name="budget_delete"),
]

from django.urls import path

from . import views
from .views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryUpdateView,
    PaymentMethodCreateView,
    PaymentMethodDeleteView,
    PaymentMethodListView,
    PaymentMethodUpdateView,
)

app_name = "expenses"

urlpatterns = [
    path("", views.expense_list, name="expense_list"),
    path("create/", views.expense_create, name="expense_create"),
    path("update/<int:pk>/", views.expense_update, name="expense_update"),
    path("delete/<int:pk>/", views.expense_delete, name="expense_delete"),
    path("sync-sheet/", views.sync_google_sheet_view, name="sync_google_sheet"),
    path("dashboard/", views.dashboard, name="dashboard"),
    # Category URLs
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/create/", CategoryCreateView.as_view(), name="category_create"),
    path(
        "categories/update/<int:pk>/",
        CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "categories/delete/<int:pk>/",
        CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    # Payment Method URLs
    path(
        "payment-methods/", PaymentMethodListView.as_view(), name="paymentmethod_list"
    ),
    path(
        "payment-methods/create/",
        PaymentMethodCreateView.as_view(),
        name="paymentmethod_create",
    ),
    path(
        "payment-methods/update/<int:pk>/",
        PaymentMethodUpdateView.as_view(),
        name="paymentmethod_update",
    ),
    path(
        "payment-methods/delete/<int:pk>/",
        PaymentMethodDeleteView.as_view(),
        name="paymentmethod_delete",
    ),
]

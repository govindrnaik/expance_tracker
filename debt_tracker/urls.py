from django.urls import path

from .views import (
    DebtCreateView,
    DebtDeleteView,
    DebtDetailView,
    DebtListView,
    DebtUpdateView,
    PaymentCreateView,
)

app_name = "debt_tracker"

urlpatterns = [
    path("", DebtListView.as_view(), name="debt_list"),
    path("<int:pk>/", DebtDetailView.as_view(), name="debt_detail"),
    path("create/", DebtCreateView.as_view(), name="debt_create"),
    path("<int:pk>/update/", DebtUpdateView.as_view(), name="debt_update"),
    path("<int:pk>/delete/", DebtDeleteView.as_view(), name="debt_delete"),
    path("<int:debt_pk>/add-payment/", PaymentCreateView.as_view(), name="add_payment"),
]

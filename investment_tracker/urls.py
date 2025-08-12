from django.urls import path

from .views import (
    InvestmentCreateView,
    InvestmentDeleteView,
    InvestmentListView,
    InvestmentTypeCreateView,
    InvestmentTypeDeleteView,
    InvestmentTypeListView,
    InvestmentTypeUpdateView,
    InvestmentUpdateView,
    PlatformCreateView,
    PlatformDeleteView,
    PlatformListView,
    PlatformUpdateView,
)

app_name = "investment_tracker"

urlpatterns = [
    path("", InvestmentListView.as_view(), name="investment_list"),
    path("create/", InvestmentCreateView.as_view(), name="investment_create"),
    path("<int:pk>/update/", InvestmentUpdateView.as_view(), name="investment_update"),
    path("<int:pk>/delete/", InvestmentDeleteView.as_view(), name="investment_delete"),
    path("platforms/", PlatformListView.as_view(), name="platform_list"),
    path("platforms/create/", PlatformCreateView.as_view(), name="platform_create"),
    path(
        "platforms/<int:pk>/update/",
        PlatformUpdateView.as_view(),
        name="platform_update",
    ),
    path(
        "platforms/<int:pk>/delete/",
        PlatformDeleteView.as_view(),
        name="platform_delete",
    ),
    path("types/", InvestmentTypeListView.as_view(), name="investmenttype_list"),
    path(
        "types/create/",
        InvestmentTypeCreateView.as_view(),
        name="investmenttype_create",
    ),
    path(
        "types/<int:pk>/update/",
        InvestmentTypeUpdateView.as_view(),
        name="investmenttype_update",
    ),
    path(
        "types/<int:pk>/delete/",
        InvestmentTypeDeleteView.as_view(),
        name="investmenttype_delete",
    ),
]

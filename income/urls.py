# d:\govind_data\playground\expance_tracker\income\urls.py
from django.urls import path

from .views import (
    IncomeCreateView,
    IncomeDeleteView,
    IncomeListView,
    IncomeUpdateView,
    SourceCreateView,
    SourceDeleteView,
    SourceListView,
    SourceUpdateView,
)

app_name = "income"

urlpatterns = [
    path("", IncomeListView.as_view(), name="income_list"),
    path("create/", IncomeCreateView.as_view(), name="income_create"),
    path("<int:pk>/update/", IncomeUpdateView.as_view(), name="income_update"),
    path("<int:pk>/delete/", IncomeDeleteView.as_view(), name="income_delete"),
    path("sources/", SourceListView.as_view(), name="source_list"),
    path("sources/create/", SourceCreateView.as_view(), name="source_create"),
    path("sources/<int:pk>/update/", SourceUpdateView.as_view(), name="source_update"),
    path("sources/<int:pk>/delete/", SourceDeleteView.as_view(), name="source_delete"),
]

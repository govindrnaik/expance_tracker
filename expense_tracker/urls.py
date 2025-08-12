"""
URL configuration for expense_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("expenses/", include("expenses.urls")),
    path("budgeting/", include("budgeting.urls")),
    path("investments/", include("investment_tracker.urls")),
    path("debts/", include("debt_tracker.urls")),
    path("income/", include("income.urls")),
    path("settings/", include("settings.urls")),
    path("", include("expenses.urls")),
]

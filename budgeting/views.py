from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import BudgetForm
from .models import Budget


class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = "budgeting/budget_list.html"
    context_object_name = "budgets"

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)


class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    form_class = BudgetForm
    template_name = "budgeting/budget_form.html"
    success_url = reverse_lazy("budgeting:budget_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BudgetUpdateView(LoginRequiredMixin, UpdateView):
    model = Budget
    form_class = BudgetForm
    template_name = "budgeting/budget_form.html"
    success_url = reverse_lazy("budgeting:budget_list")


class BudgetDeleteView(LoginRequiredMixin, DeleteView):
    model = Budget
    template_name = "budgeting/budget_confirm_delete.html"
    success_url = reverse_lazy("budgeting:budget_list")

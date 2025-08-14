from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import DebtForm, PaymentForm
from .models import Debt, Payment


class DebtListView(LoginRequiredMixin, ListView):
    model = Debt
    template_name = "debt_tracker/debt_list.html"
    context_object_name = "debts"

    def get_queryset(self):
        return Debt.objects.filter(user=self.request.user)


class DebtDetailView(LoginRequiredMixin, DetailView):
    model = Debt
    template_name = "debt_tracker/debt_detail.html"
    context_object_name = "debt"

    def get_queryset(self):
        return Debt.objects.filter(user=self.request.user)


class DebtCreateView(LoginRequiredMixin, CreateView):
    model = Debt
    form_class = DebtForm
    template_name = "debt_tracker/debt_form.html"
    success_url = reverse_lazy("debt_tracker:debt_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DebtUpdateView(LoginRequiredMixin, UpdateView):
    model = Debt
    form_class = DebtForm
    template_name = "debt_tracker/debt_form.html"
    success_url = reverse_lazy("debt_tracker:debt_list")

    def get_queryset(self):
        return Debt.objects.filter(user=self.request.user)


class DebtDeleteView(LoginRequiredMixin, DeleteView):
    model = Debt
    template_name = "debt_tracker/debt_confirm_delete.html"
    success_url = reverse_lazy("debt_tracker:debt_list")

    def get_queryset(self):
        return Debt.objects.filter(user=self.request.user)


class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = "debt_tracker/payment_form.html"

    def form_valid(self, form):
        debt = get_object_or_404(
            Debt, pk=self.kwargs["debt_pk"], user=self.request.user
        )
        form.instance.debt = debt
        debt.amount_paid += form.instance.amount
        debt.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "debt_tracker:debt_detail", kwargs={"pk": self.kwargs["debt_pk"]}
        )

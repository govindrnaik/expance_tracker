from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import IncomeForm, SourceForm
from .models import Income, Source


# Income Views
class IncomeListView(LoginRequiredMixin, ListView):
    model = Income
    template_name = "income/income_list.html"
    context_object_name = "incomes"

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)


class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    form_class = IncomeForm
    template_name = "income/income_form.html"
    success_url = reverse_lazy("income:income_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = "income/income_form.html"
    success_url = reverse_lazy("income:income_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)


class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Income
    template_name = "income/income_confirm_delete.html"
    success_url = reverse_lazy("income:income_list")

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)


# Source Views
class SourceListView(LoginRequiredMixin, ListView):
    model = Source
    template_name = "income/source_list.html"
    context_object_name = "sources"

    def get_queryset(self):
        return Source.objects.filter(user=self.request.user)


class SourceCreateView(LoginRequiredMixin, CreateView):
    model = Source
    form_class = SourceForm
    template_name = "income/source_form.html"
    success_url = reverse_lazy("income:source_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SourceUpdateView(LoginRequiredMixin, UpdateView):
    model = Source
    form_class = SourceForm
    template_name = "income/source_form.html"
    success_url = reverse_lazy("income:source_list")

    def get_queryset(self):
        return Source.objects.filter(user=self.request.user)


class SourceDeleteView(LoginRequiredMixin, DeleteView):
    model = Source
    template_name = "income/source_confirm_delete.html"
    success_url = reverse_lazy("income:source_list")

    def get_queryset(self):
        return Source.objects.filter(user=self.request.user)

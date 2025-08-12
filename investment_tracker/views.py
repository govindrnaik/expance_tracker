from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import InvestmentForm, InvestmentTypeForm, PlatformForm
from .models import Investment, InvestmentType, Platform


class InvestmentListView(LoginRequiredMixin, ListView):
    model = Investment
    template_name = "investment_tracker/investment_list.html"
    context_object_name = "investments"

    def get_queryset(self):
        return Investment.objects.filter(user=self.request.user)


class InvestmentCreateView(LoginRequiredMixin, CreateView):
    model = Investment
    form_class = InvestmentForm
    template_name = "investment_tracker/investment_form.html"
    success_url = reverse_lazy("investment_tracker:investment_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class InvestmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Investment
    form_class = InvestmentForm
    template_name = "investment_tracker/investment_form.html"
    success_url = reverse_lazy("investment_tracker:investment_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class InvestmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Investment
    template_name = "investment_tracker/investment_confirm_delete.html"
    success_url = reverse_lazy("investment_tracker:investment_list")


class PlatformListView(LoginRequiredMixin, ListView):
    model = Platform
    template_name = "investment_tracker/platform_list.html"
    context_object_name = "platforms"

    def get_queryset(self):
        return Platform.objects.filter(user=self.request.user)


class PlatformCreateView(LoginRequiredMixin, CreateView):
    model = Platform
    form_class = PlatformForm
    template_name = "investment_tracker/platform_form.html"
    success_url = reverse_lazy("investment_tracker:platform_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlatformUpdateView(LoginRequiredMixin, UpdateView):
    model = Platform
    form_class = PlatformForm
    template_name = "investment_tracker/platform_form.html"
    success_url = reverse_lazy("investment_tracker:platform_list")


class PlatformDeleteView(LoginRequiredMixin, DeleteView):
    model = Platform
    template_name = "investment_tracker/platform_confirm_delete.html"
    success_url = reverse_lazy("investment_tracker:platform_list")


class InvestmentTypeListView(LoginRequiredMixin, ListView):
    model = InvestmentType
    template_name = "investment_tracker/investmenttype_list.html"
    context_object_name = "investment_types"

    def get_queryset(self):
        return InvestmentType.objects.filter(user=self.request.user)


class InvestmentTypeCreateView(LoginRequiredMixin, CreateView):
    model = InvestmentType
    form_class = InvestmentTypeForm
    template_name = "investment_tracker/investmenttype_form.html"
    success_url = reverse_lazy("investment_tracker:investmenttype_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class InvestmentTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = InvestmentType
    form_class = InvestmentTypeForm
    template_name = "investment_tracker/investmenttype_form.html"
    success_url = reverse_lazy("investment_tracker:investmenttype_list")


class InvestmentTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = InvestmentType
    template_name = "investment_tracker/investmenttype_confirm_delete.html"
    success_url = reverse_lazy("investment_tracker:investmenttype_list")

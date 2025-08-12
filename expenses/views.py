from datetime import datetime

import pandas as pd
import plotly.express as px
import plotly.io as pio
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from budgeting.models import Budget

from .forms import CategoryForm, ExpenseForm, PaymentMethodForm
from .models import Category, Expense, PaymentMethod
from .services import add_expense_to_sheet, sync_expenses_to_sheet


@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, "expenses/expense_list.html", {"expenses": expenses})


@login_required
def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST, user=request.user)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            add_expense_to_sheet(expense)
            return redirect("expense_list")
    else:
        form = ExpenseForm(user=request.user)
    return render(request, "expenses/expense_form.html", {"form": form})


@login_required
def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense, user=request.user)
        if form.is_valid():
            form.save()
            sync_expenses_to_sheet(
                request.user, Expense.objects.filter(user=request.user)
            )
            return redirect("expense_list")
    else:
        form = ExpenseForm(instance=expense, user=request.user)
    return render(request, "expenses/expense_form.html", {"form": form})


@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == "POST":
        expense.delete()
        sync_expenses_to_sheet(request.user, Expense.objects.filter(user=request.user))
        return redirect("expense_list")
    return render(request, "expenses/expense_confirm_delete.html", {"expense": expense})


@login_required
def sync_google_sheet_view(request):
    """
    A view to manually trigger a full sync of expenses to Google Sheets.
    """
    expenses = Expense.objects.filter(user=request.user)
    sync_expenses_to_sheet(request.user, expenses)
    return redirect("expense_list")


@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user).select_related(
        "category", "payment_mode"
    )
    total_expenses = expenses.aggregate(Sum("amount"))["amount__sum"] or 0

    # Budget data
    now = datetime.now()
    budgets = Budget.objects.filter(user=request.user, year=now.year, month=now.month)
    budget_data = []
    for budget in budgets:
        spent = (
            expenses.filter(
                category=budget.category,
                date__year=now.year,
                date__month=now.month,
            ).aggregate(Sum("amount"))["amount__sum"]
            or 0
        )
        remaining = budget.amount - spent
        budget_data.append(
            {
                "category": budget.category.name,
                "budget": budget.amount,
                "spent": spent,
                "remaining": remaining,
            }
        )

    category_chart_div = None
    time_chart_div = None

    # Get theme from cookie, default to 'light'
    theme = request.COOKIES.get("theme", "light")
    plotly_template = "plotly_dark" if theme == "dark" else "plotly_white"

    if expenses.exists():
        # Prepare data for charts, ensuring 'category' is handled correctly
        df_data = []
        for expense in expenses:
            df_data.append(
                {
                    "category": expense.category.name
                    if expense.category
                    else "Uncategorized",
                    "amount": expense.amount,
                    "date": expense.date,
                    "payment_mode": expense.payment_mode.name
                    if expense.payment_mode
                    else "N/A",
                }
            )
        df = pd.DataFrame(df_data)

        df["amount"] = pd.to_numeric(df["amount"])
        df["date"] = pd.to_datetime(df["date"])

        # 1. Category Summary Chart (Bar Chart)
        category_summary = (
            df.groupby("category")["amount"]
            .sum()
            .reset_index()
            .sort_values(by="amount", ascending=False)
        )
        # category_summary["amount"] = pd.to_numeric(
        #     category_summary["amount"], errors="raise"
        # )

        fig_cat = px.bar(
            category_summary,
            x="category",
            y="amount",
            title="Total Expenses by Category",
            labels={"category": "Category", "amount": "Total Amount"},
            template=plotly_template,  # or your plotly_template
        )

        fig_cat.update_layout(
            xaxis_title="",
            yaxis_title="Amount",
            yaxis=dict(tickformat=",.2f"),
            title_x=0.5,
            margin=dict(l=20, r=20, t=40, b=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        # If this is the first chart on the page, set True; otherwise False
        category_chart_div = pio.to_html(
            fig_cat, full_html=False, include_plotlyjs=True
        )

        # 2. Time-Based Spending Chart (Line Chart)
        # Group by day and sum amounts
        time_summary = df.groupby(df["date"].dt.date)["amount"].sum().reset_index()

        fig_time = px.line(
            time_summary,
            x="date",
            y="amount",
            title="Daily Spending Over Time",
            labels={"date": "Date", "amount": "Total Amount Spent"},
            template=plotly_template,
            markers=True,  # Add markers to data points
        )
        fig_time.update_layout(
            xaxis_title="",
            yaxis_title="Amount",
            title_x=0.5,
            margin=dict(l=20, r=20, t=40, b=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )
        time_chart_div = pio.to_html(fig_time, full_html=False, include_plotlyjs=False)

    return render(
        request,
        "expenses/dashboard.html",
        {
            "total_expenses": total_expenses,
            "budget_data": budget_data,
            "category_chart_div": category_chart_div,
            "time_chart_div": time_chart_div,
            # Pass a flag to include the Plotly JS file once in the template
            "include_plotly_js": True,
        },
    )


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "expenses/category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "expenses/category_form.html"
    success_url = reverse_lazy("category_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "expenses/category_form.html"
    success_url = reverse_lazy("category_list")

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "expenses/category_confirm_delete.html"
    success_url = reverse_lazy("category_list")

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class PaymentMethodListView(LoginRequiredMixin, ListView):
    model = PaymentMethod
    template_name = "expenses/paymentmethod_list.html"
    context_object_name = "payment_methods"

    def get_queryset(self):
        return PaymentMethod.objects.filter(user=self.request.user)


class PaymentMethodCreateView(LoginRequiredMixin, CreateView):
    model = PaymentMethod
    form_class = PaymentMethodForm
    template_name = "expenses/paymentmethod_form.html"
    success_url = reverse_lazy("paymentmethod_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PaymentMethodUpdateView(LoginRequiredMixin, UpdateView):
    model = PaymentMethod
    form_class = PaymentMethodForm
    template_name = "expenses/paymentmethod_form.html"
    success_url = reverse_lazy("paymentmethod_list")

    def get_queryset(self):
        return PaymentMethod.objects.filter(user=self.request.user)


class PaymentMethodDeleteView(LoginRequiredMixin, DeleteView):
    model = PaymentMethod
    template_name = "expenses/paymentmethod_confirm_delete.html"
    success_url = reverse_lazy("paymentmethod_list")

    def get_queryset(self):
        return PaymentMethod.objects.filter(user=self.request.user)

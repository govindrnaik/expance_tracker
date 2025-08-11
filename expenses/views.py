import pandas as pd
import plotly.express as px
import plotly.io as pio
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ExpenseForm
from .models import Expense
from .services import add_expense_to_sheet, sync_expenses_to_sheet


@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, "expenses/expense_list.html", {"expenses": expenses})


@login_required
def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            add_expense_to_sheet(expense)
            return redirect("expense_list")
    else:
        form = ExpenseForm()
    return render(request, "expenses/expense_form.html", {"form": form})


@login_required
def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            sync_expenses_to_sheet(
                request.user, Expense.objects.filter(user=request.user)
            )
            return redirect("expense_list")
    else:
        form = ExpenseForm(instance=expense)
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
    expenses = Expense.objects.filter(user=request.user)
    total_expenses = expenses.aggregate(Sum("amount"))["amount__sum"] or 0
    category_chart_div = None
    time_chart_div = None

    # Get theme from cookie, default to 'light'
    theme = request.COOKIES.get("theme", "light")
    plotly_template = "plotly_dark" if theme == "dark" else "plotly_white"

    if expenses.exists():
        df = pd.DataFrame(list(expenses.values("category", "amount", "date")))
        df["amount"] = pd.to_numeric(df["amount"])
        df["date"] = pd.to_datetime(df["date"])
        df["category"] = df["category"].str.lower()

        # 1. Category Summary Chart (Bar Chart)
        category_summary = (
            df.groupby("category")["amount"]
            .sum()
            .reset_index()
            .sort_values(by="amount", ascending=True)
        )
        fig_cat = px.bar(
            category_summary,
            x="category",
            y="amount",
            title="Total Expenses by Category",
            labels={"category": "Category", "amount": "Total Amount"},
            template=plotly_template,
        )
        fig_cat.update_layout(
            xaxis_title="",
            yaxis_title="Amount",
            yaxis=dict(tickformat=".2f"),
            title_x=0.5,
            margin=dict(l=20, r=20, t=40, b=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )
        # We pass include_plotlyjs=False for subsequent charts
        category_chart_div = pio.to_html(
            fig_cat, full_html=False, include_plotlyjs=False
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
            "category_chart_div": category_chart_div,
            "time_chart_div": time_chart_div,
            # Pass a flag to include the Plotly JS file once in the template
            "include_plotly_js": True,
        },
    )

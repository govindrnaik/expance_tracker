import os

import gspread
from django.conf import settings
from oauth2client.service_account import ServiceAccountCredentials

# --- NEW CONFIGURATION ---
# We will use one master spreadsheet for the entire application.
MASTER_SPREADSHEET_NAME = "Expense Tracker"
CREDENTIALS_FILE = os.path.join(settings.BASE_DIR, "credentials.json")


def get_or_create_worksheet(user):
    """
    Connects to the master spreadsheet and gets or creates a worksheet (tab) for the user.
    """
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)

    # Open the master spreadsheet or create it if it doesn't exist.
    try:
        spreadsheet = client.open(MASTER_SPREADSHEET_NAME)
    except gspread.exceptions.SpreadsheetNotFound:
        spreadsheet = client.create(MASTER_SPREADSHEET_NAME)
        # Share the master sheet with your main email so you can easily view it.
        # IMPORTANT: Replace with your actual email address in settings.py
        owner_email = getattr(settings, "GOOGLE_SHEETS_OWNER_EMAIL", None)
        if owner_email:
            spreadsheet.share(owner_email, perm_type="user", role="owner")

    # Get or create the worksheet for the specific user.
    worksheet_title = user.username
    try:
        worksheet = spreadsheet.worksheet(worksheet_title)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(
            title=worksheet_title, rows="100", cols="20"
        )

    return worksheet


def ensure_header(sheet):
    """Ensures the worksheet has the correct header row."""
    header = ["Date", "Category", "Amount", "Description"]
    # Check if the first row is empty or doesn't match the header
    first_row = sheet.row_values(1)
    if not first_row or first_row != header:
        # Prepend the header if it's missing or incorrect
        sheet.insert_row(header, 1)
        # If the first row was not empty, it means it was data.
        # We need to check if the row we just pushed down is now a duplicate header.
        # This can happen if the sheet was created but header writing failed.
        if len(sheet.row_values(2)) > 0 and sheet.row_values(2) == header:
            sheet.delete_rows(2)


def add_expense_to_sheet(expense):
    """Appends a single new expense to the user's worksheet."""
    try:
        worksheet = get_or_create_worksheet(expense.user)
        ensure_header(worksheet)
        row = [
            str(expense.date),
            expense.category,
            float(expense.amount),
            expense.description,
        ]
        worksheet.append_row(row)
        print(
            f"Successfully added expense to worksheet for {expense.user.username}: {row}"
        )
    except Exception as e:
        print(f"Error adding expense to worksheet for {expense.user.username}: {e}")


def sync_expenses_to_sheet(user, expenses):
    """
    Overwrites the user's worksheet with the complete, current list of expenses.
    """
    try:
        worksheet = get_or_create_worksheet(user)
        worksheet.clear()
        ensure_header(worksheet)

        all_rows = [
            [str(exp.date), exp.category, float(exp.amount), exp.description]
            for exp in expenses
        ]

        if all_rows:
            # Use 'USER_ENTERED' to ensure correct type parsing in Google Sheets
            worksheet.append_rows(all_rows, value_input_option="USER_ENTERED")

        print(
            f"Successfully synced {len(expenses)} expenses to worksheet for {user.username}."
        )
    except Exception as e:
        print(f"Error syncing expenses to worksheet for {user.username}: {e}")

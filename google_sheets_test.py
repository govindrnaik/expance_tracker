import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# --- INSTRUCTIONS ---
# 1. Make sure your credentials.json file is in the same directory as this script.
# 2. Replace 'Your-Spreadsheet-Name' with the exact name of your Google Sheet.
# 3. Run this script from your terminal: .\\.venv\\Scripts\\activate.bat && python google_sheets_test.py

SPREADSHEET_NAME = "Expense Tracker"
CREDENTIALS_FILE = "credentials.json"


def test_google_sheets_connection():
    """
    Tests the connection to Google Sheets using service account credentials.
    """
    print("--- Starting Google Sheets Connection Test ---")

    # Check if credentials file exists
    if not os.path.exists(CREDENTIALS_FILE):
        print(
            f"Error: Credentials file not found at '{os.path.abspath(CREDENTIALS_FILE)}'"
        )
        print(
            "Please make sure your 'credentials.json' file is in the project root directory."
        )
        return

    print(f"Found credentials file: '{CREDENTIALS_FILE}'")

    # Define the scope
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    try:
        # Add credentials to the account
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE, scope
        )

        # Authorize the clientsheet
        client = gspread.authorize(creds)
        print("Successfully authorized with Google.")

        # Open the spreadsheet
        print(f"Trying to open spreadsheet: '{SPREADSHEET_NAME}'...")
        sheet = client.open(SPREADSHEET_NAME).sheet1

        print("\n--- SUCCESS! ---")
        print("Successfully connected to your Google Sheet.")
        print("Your credentials are correct and the sheet is shared properly.")

        # You can optionally add a test write here
        # sheet.update_acell('A1', 'Test successful!')
        # print("Test write to cell A1 was successful.")

    except gspread.exceptions.SpreadsheetNotFound:
        print("\n--- ERROR: Spreadsheet Not Found ---")
        print(f"Could not find a spreadsheet named '{SPREADSHEET_NAME}'.")
        print("Please check the following:")
        print("1. Is the SPREADSHEET_NAME in this script spelled correctly?")
        print("2. Is the spreadsheet in your Google Drive?")

    except Exception as e:
        print(f"\n--- AN ERROR OCCURRED ---")
        print(f"Error details: {e}")
        print("\nPlease check the following:")
        print(
            "1. Did you enable the 'Google Drive API' and 'Google Sheets API' in your Google Cloud project?"
        )
        print(
            f"2. Did you share your spreadsheet with the client_email from your credentials file?"
        )
        print(
            "   - The email is likely something like: your-service-account@your-project.iam.gserviceaccount.com"
        )
        print("   - Make sure you gave it 'Editor' permissions.")


if __name__ == "__main__":
    if SPREADSHEET_NAME == "Your-Spreadsheet-Name":
        print(
            "Please open 'google_sheets_test.py' and replace 'Your-Spreadsheet-Name' with the actual name of your sheet before running."
        )
    else:
        test_google_sheets_connection()

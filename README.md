# Expense Tracker

A personal expense tracker Django project for locally storing and recording daily expenses.

## Features

* **User Authentication:** Secure user registration and login system.
* **Full CRUD Functionality:** Create, Read, Update, and Delete expenses.
* **Detailed Expense Entry:** Record expenses with fields for date, time, category, sub-category, description, amount, expiry date, and payment mode.
* **Category and Payment Method Management:** Users can create and manage their own expense categories and payment methods.
* **Dashboard:** Provides an overview and analysis of your expenses with charts and summaries.
* **View Reports:** Visualize your spending with daily, weekly, and monthly reports.
* **Dual Database System:** Uses a public Google Sheet as the primary database and a local SQLite database for backup.

## Core Applications

* **Dashboard:** Provides an overview and analysis of your expenses with charts and summaries.
* **Expenses:** Full CRUD functionality for managing expenses, categories, and payment methods.
* **Reports:** Generate detailed reports of your spending habits.
* **Users:** Handles user registration and authentication.

## Software Stack

* **Backend:** Django
* **Database:** Google Sheets (Primary), SQLite (Backup)
* **Frontend:** Django Templates, HTML, CSS, JavaScript

## Completed Features

* [x] **Category Management:** Allowing users to create and manage their own categories.
* [x] **Detailed Expense Fields:** Adding more fields to the expense model like sub-category, expiry date, and payment mode.
* [x] **Payment Method Management:** Allowing users to create and manage their own payment methods.

## To-Do List

* [ ] Enhance the frontend with a more modern UI/UX.
* [ ] Add more advanced reporting features (e.g., filtering by date range, exporting to CSV).
* [ ] Implement password reset functionality.
* [ ] Write comprehensive tests.

## Prerequisites

This project uses [uv](https://github.com/astral-sh/uv) for Python packaging and environment management. Make sure you have it installed before proceeding.

## Setup and Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/govindrnaik/expance_tracker.git
    cd expance_tracker
    ```

2. **Sync dependencies using `uv`:**

    ```bash
    uv sync
    ```

3. **Configure your database:**
    Create a `.env` file in the project root and add the public URL of your Google Sheet.

    ```
    # .env
    GOOGLE_SHEET_URL=your_public_google_sheet_link_here
    ```

4. **Run database migrations for the local backup:**

    ```bash
    uv run python manage.py migrate
    ```

5. **Start the development server:**

    ```bash
    uv run python manage.py runserver
    ```

6. **Create super user:**

    ```bash
    uv run python manage.py createsuperuser
    ```

7. **Add dummy expenses (optional):**

    ```bash
    uv run python manage.py add_dummy_expenses <username> <count>
    ```

    This command adds dummy expenses for testing purposes. Replace `<username>` with the desired username and `<count>` with the number of dummy expenses you want to create.

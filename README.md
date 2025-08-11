# Expense Tracker

A personal expense tracker Django project for locally storing and recording daily expenses.

## Features

* **User Authentication:** Secure user registration and login system.
* **Full CRUD Functionality:** Create, Read, Update, and Delete expenses.
* **Categorize Expenses:** Organize your expenses into different categories for better tracking.
* **Dashboard:** Provides an overview and analysis of your expenses with charts and summaries.
* **View Reports:** Visualize your spending with daily, weekly, and monthly reports.
* **Dual Database System:** Uses a public Google Sheet as the primary database and a local SQLite database for backup.

## Core Applications

* **Dashboard:** Provides an overview and analysis of your expenses with charts and summaries.
* **Expenses:** Full CRUD functionality for managing expenses.
* **Reports:** Generate detailed reports of your spending habits.
* **Users:** Handles user registration and authentication.

## Software Stack

* **Backend:** Django
* **Database:** Google Sheets (Primary), SQLite (Backup)
* **Frontend:** Django Templates, HTML, CSS, JavaScript

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
    git clone https://github.com/your-username/expance_tracker.git
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
    python manage.py migrate
    ```

5. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

# Expense Tracker

A personal expense tracker Django project for locally storing and recording daily expenses.

## Features

* **Record Daily Expenses:** Easily add and manage your daily expenses.
* **Categorize Expenses:** Organize your expenses into different categories for better tracking.
* **View Reports:** Visualize your spending with daily, weekly, and monthly reports.
* **Dual Database System:** Uses a public Google Sheet as the primary database and a local SQLite database for backup.

## Core Applications

* **Dashboard:** Provides an overview and analysis of your expenses with charts and summaries.
* **Expense Entry:** A simple form to quickly add new expenses.
* **Reports:** Generate detailed reports of your spending habits over time.

## Software Stack

* **Backend:** Django
* **Database:** Google Sheets (Primary), SQLite (Backup)
* **Frontend:** Django Templates, HTML, CSS, JavaScript

## To-Do List

* [ ] User authentication system.
* [ ] Implement full CRUD (Create, Read, Update, Delete) functionality for expenses.
* [ ] Integrate with the Google Sheets API for data synchronization.
* [ ] Develop different report views (e.g., by category, by date range).
* [ ] Enhance the frontend with a modern UI/UX.
* [ ] Add data visualization with charts and graphs.

## Prerequisites

This project uses [uv](https://github.com/astral-sh/uv) for Python packaging and environment management. Make sure you have it installed before proceeding.

## Setup and Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/expance_tracker.git
    cd expance_tracker
    ```

2. **Create and activate a virtual environment using `uv`:**

    ```bash
    uv venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Sync dependencies using `uv`:**

    ```bash
    uv pip sync requirements.txt
    ```

4. **Configure your database:**
    Create a `.env` file in the project root and add the public URL of your Google Sheet.

    ```
    # .env
    GOOGLE_SHEET_URL=your_public_google_sheet_link_here
    ```

5. **Run database migrations for the local backup:**

    ```bash
    python manage.py migrate
    ```

6. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

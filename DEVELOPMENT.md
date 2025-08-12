# Expense Tracker: Development and Feature Summary

This document outlines the features and development process for the Expense Tracker application.

## Core Features

The application is built with a robust set of features to provide a comprehensive expense tracking experience.

* [x] **Full User Authentication**
  * Secure user registration, login, and logout functionality.
  * Expenses are tied to individual user accounts.

* [x] **Complete Expense Management (CRUD)**
  * Users can create, view, update, and delete their expenses.
  * An intuitive interface for managing expense records.

* [x] **Detailed Expense Entry**
  * Each expense entry will include:
    * Date and Time
    * Category (user-created)
    * Sub-category (free text)
    * Description
    * Amount
    * Expiry Date
    * Payment Mode (user-created)

* [x] **Dynamic, Interactive Reporting**
  * A reporting dashboard with an interactive bar chart visualizing expenses by category.
  * Built with Plotly for a rich, engaging user experience.

* [x] **Seamless Google Sheets Integration**
  * Each user is automatically provided with their own personal Google Sheet.
  * The application automatically creates the sheet and shares it with the user's email.
  * Data is kept in sync:
    * Creating an expense instantly adds it to the sheet.
    * Updating or deleting an expense triggers a full resync to ensure data integrity.
    * A manual "Sync" button is available for on-demand synchronization.

* [x] **Modern, Responsive User Interface**
  * Styled with Bootstrap 5 for a clean, professional, and responsive design that works on all devices.
  * Includes a full-featured navigation bar for easy access to all sections.
  * **Theme-Aware Dark Mode**:
    * A dark mode toggle allows users to switch between light and dark themes.
    * The selected theme is saved, providing a consistent experience across sessions.
    * Interactive charts automatically adapt to the chosen theme.

* [x] **Developer-Friendly Features**
  * Includes a custom Django management command to easily populate the database with dummy data for testing and demonstration.

## Project Status

| Feature | Status | Notes |
| --- | --- | --- |
| User Authentication | `Done` | Secure registration, login, and logout. |
| Expense CRUD | `Done` | Full create, read, update, and delete functionality for expenses. |
| Category Management | `Done` | Users can create and manage their own expense categories. |
| Payment Method Management | `Done` | Users can create and manage their own payment methods. |
| Detailed Expense Entry | `Done` | Expanding expense model with more detailed fields. |
| Google Sheets Integration | `Done` | Robust, per-user syncing with automatic header and data management. |
| Reporting & Visualization | `Done` | Interactive, theme-aware charts using Plotly. |
| UI/UX and Dark Mode | `Done` | Modern, responsive design with Bootstrap 5 and a dark mode toggle. |
| **Overall Project** | `In Progress` | Core features are implemented, new features are in development. |

---

This project was developed step-by-step, ensuring each feature was built, tested, and refined before moving to the next.

## Future Development

Here are the planned features and enhancements for future releases:

* **Enhance Payment Methods:**
  * [x] Add a `description` field to the `PaymentMethod` model to store additional details.

* **New Applications:**
  * [ ] **Investment Tracker:** A flexible app to track investments.
    * [ ] Create `Platform` model for users to manage their investment platforms (e.g., Fidelity, Coinbase).
    * [ ] Create `InvestmentType` model for users to manage different types of investments (e.g., Stocks, Crypto).
    * [ ] Create `Investment` model to log individual investment transactions.
    * [ ] Implement full CRUD functionality for Platforms, Investment Types, and Investments.
    * [ ] Build the user interface for managing all aspects of the investment tracker.
  * [ ] **Debt Tracker:** An application to manage and monitor outstanding debts, such as loans and credit card balances.
  * [ ] **Budgeting Tool:** A comprehensive budgeting app to help users set financial goals and track their progress.
  * [x] **Settings Page:** A dedicated page for users to configure application settings.
    * [ ] Add an option to manage database credentials.
    * [x] Add an option to change the linked Google Sheet URL.

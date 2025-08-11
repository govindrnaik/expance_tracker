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

| Feature                       | Status | Notes                                                              |
| ----------------------------- | ------ | ------------------------------------------------------------------ |
| User Authentication           | `Done` | Secure registration, login, and logout.                            |
| Expense CRUD                  | `Done` | Full create, read, update, and delete functionality for expenses.  |
| Google Sheets Integration     | `Done` | Robust, per-user syncing with automatic header and data management.|
| Reporting & Visualization     | `Done` | Interactive, theme-aware charts using Plotly.                      |
| UI/UX and Dark Mode           | `Done` | Modern, responsive design with Bootstrap 5 and a dark mode toggle. |
| **Overall Project**           | `Done` | All core features are implemented and polished.                    |

---

This project was developed step-by-step, ensuring each feature was built, tested, and refined before moving to the next.

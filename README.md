# Expense Tracker

An Expense Tracker is a simple Python application that helps you keep track of your expenses and manage your budget. It uses SQLite3 for local database management to store and retrieve expense data.

## Features

- **Add New Expenses**: Enter details such as amount, category, and date.
- **View Expenses**: List all recorded expenses.
- **Filter Expenses**: Search by category and date range.
- **Edit and Delete**: Modify or remove existing expenses.
- **Summary**: Get a summary of expenses by category and date.

## Technologies

- **Python**: The core language used for development.
- **SQLite3**: Lightweight database engine used to store expense records.
- **Docker**: Used to containerize the app and make it portable and easy to run in any environment.

## Dockerfile
This project includes a `Dockerfile` that allows you to easily run the Expense Tracker app within a Docker container. The Dockerfile is configured to create a container that:

1. Uses the official Python 3.10-slim image.
2. Copies the application files (`main.py` and `db_maker.py`) into the container.
3. Sets up a volume to store the database file (`expenses.db`).
4. Runs the `db_maker.py` script to initialize the database and prepares the app for usage.
5. Runs the `main.py` script to start the app.

To build and run the app with Docker run the command 
```bash run_docker.sh```

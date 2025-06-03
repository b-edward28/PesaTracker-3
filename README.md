# PesaTracker

**Owner**: Brendah Chepngeno

PesaTracker is a command-line application designed to help users track their personal expenses, stay within budget, and make informed financial decisions. It allows users to register, log in, set budgets by category, and manage their spending records.

---

## Features

- **Register User**: Users can create an account by providing their name and email.
- **Login User**: Existing users can log in to access their budgets and expenses.
- **Set Budgets**: Users set a monthly budget per expense category.
- **Add New Expense**: Log new expenses with category, amount, description, and date.
- **View All Expenses**: Display a list of all recorded expenses by the user.
- **Delete an Expense**: Remove a selected expense from the record.
- **Budget Alerts**: Notify users when their expenses exceed set budgets.

---

## Technologies Used

- **Python** – Core language used for development.
- **SQLAlchemy** – ORM for handling the database models and queries.
- **SQLite** – Lightweight relational database used for storing user and expense data.
- **Alembic** – For managing database migrations.
- **Pipenv** – For virtual environment and dependency management.

---

## Setup Instructions

1. **Clone the Repository**

git clone this repository
cd PesaTracker

2. **Install dependancies**

pipenv install

3. **Install Alembic for migrations**

pipenv install alembic 

4. **Activate the virtual Environment**

pipenv shell

5. **Run Migrations**

alembic upgrade head

6. **Start Application**

python -m lib.cli

---

## Support/Contact

**Brendah Edward**
**Email:** edwardbrendah28@gmail.com



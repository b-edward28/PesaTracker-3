from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, extract, func
from lib.models.user import User
from lib.models.expense import Expense
from lib.models.category import Category
from lib.models.budget import Budget
from lib.models.base import Base
from datetime import datetime

# Database setup
engine = create_engine('sqlite:///pesatracker.db')
Session = sessionmaker(bind=engine)
session = Session()

# Register user
def register_user():
    print("\n--- Register New User ---")
    name = input("Enter full name: ").strip()
    email = input("Enter email: ").strip()
    user = User(name=name, email=email)

    session.add(user)
    session.commit()
    print(f"User '{name}' registered successfully.")

# Budget setup after login
def prompt_budget_setup(user):
    print("\n--- Budget Setup ---")
    categories = session.query(Category).all()

    if not categories:
        print("No categories found. Please add an expense first to create categories.")
        return

    for category in categories:
        budget = session.query(Budget).filter_by(user_id=user.id, category_id=category.id).first()
        if not budget:
            while True:
                try:
                    amount = float(input(f"Set budget for category '{category.name}': "))
                    break
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")

            new_budget = Budget(user_id=user.id, category_id=category.id, amount=amount)
            session.add(new_budget)

    session.commit()
    print("Budgets set up successfully.")

# Login user
def login_user():
    print("\n--- User Login ---")
    email = input("Enter your email: ").strip()
    name = input("Enter your full name: ").strip()
    user = session.query(User).filter_by(email=email, name=name).first()
    
    if user:
        print("Login successful. Welcome back!")
        prompt_budget_setup(user)
        return user
    else:
        print("Invalid credentials.")
        return None

# Add expense
def add_expense_for_user(user):
    print("\n--- Add New Expense ---")
    category_name = input("Enter expense category (e.g., Food, Transport): ").strip()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    description = input("Enter a short description: ").strip()
    date_str = input("Enter date (YYYY-MM-DD): ")

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        return

    # Get or create the category
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
        session.commit()

    # Check for a budget set for this category
    budget = session.query(Budget).filter_by(user_id=user.id, category_id=category.id).first()

    # Sum user's expenses in this category for the same month
    total_expenses = session.query(Expense).filter(
        Expense.user_id == user.id,
        Expense.category_id == category.id,
        extract('month', Expense.date) == date.month,
        extract('year', Expense.date) == date.year
    ).with_entities(func.sum(Expense.amount)).scalar() or 0

    new_total = total_expenses + amount

    # Check against category-specific budget
    if budget and new_total > budget.amount:
        print(f"Warning: This expense will exceed your budget for '{category_name}' (Ksh {budget.amount}).")
        confirm = input("Do you still want to add the expense? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Expense not added.")
            return

    new_expense = Expense(
        user_id=user.id,
        category=category,
        amount=amount,
        description=description,
        date=date
    )

    session.add(new_expense)
    session.commit()
    print("Expense added successfully.")

# View expenses
def view_expenses_for_user(user):
    expenses = session.query(Expense).filter_by(user_id=user.id).order_by(Expense.date.desc()).all()
    if not expenses:
        print("No expenses found.")
        return

    print(f"\n--- Expenses for {user.name} ---")
    for exp in expenses:
        print(f"{exp.date} | {exp.category} | Ksh {exp.amount} | {exp.description}")

# Delete expense
def delete_expense():
    expense_id = input("Enter the ID of the expense to delete: ")
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if not expense:
        print("Expense not found.")
        return
    session.delete(expense)
    session.commit()
    print("Expense deleted successfully.")

# Exit program
def exit_program():
    print("👋 Goodbye!")
    exit()

# Display menu
def menu():
    print("\n=== PESA TRACKER MENU ===")
    print("1. Register a new user")
    print("2. Login")
    print("3. Add new expense")
    print("4. View all expenses")
    print("5. Delete an expense")
    print("0. Exit the program")

# Main program
def main():
    current_user = None

    while True:
        menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            current_user = login_user()
        elif choice == "3":
            if current_user:
                add_expense_for_user(current_user)
            else:
                print("Please login first.")
        elif choice == "4":
            if current_user:
                view_expenses_for_user(current_user)
            else:
                print("Please login first.")
        elif choice == "5":
            delete_expense()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

# Run the CLI
if __name__ == "__main__":
    main()

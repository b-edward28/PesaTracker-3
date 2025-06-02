from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.user import User
from models.category import Category
from models.expense import Expense
from models.budget import Budget
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine("sqlite:///pesatracker.db")
session = sessionmaker(bind=engine)
session = session()

session.query(User).delete()
session.query(Category).delete()
session.query(Expense).delete()
session.query(Budget).delete()

users = [
    User(name="Joseph Kamau", email="joe@gmail.com"),
    User(name="June Moraa", email="june@gmail.com"),
    User(name="Alice Wanjala", email="alice@gmail.com")
]


categories = [
    Category(name="Food"),
    Category(name="Transport"),
    Category(name="Entertainment"),
    Category(name="Clothing"),
    Category(name="Healthcare"),
    Category(name="Utilities"),
    Category(name="Education"),
    Category(name="Housing"),
    Category(name="Miscellaneous")
]

expenses = [
    Expense(amount=100, description="Groceries", date=datetime(2023, 6, 1), category_id=1, user_id=1),
    Expense(amount=500, description="Transportation", date=datetime(2023, 6, 2), category_id=2, user_id=1),
    Expense(amount=2000, description="Movie tickets", date=datetime(2023, 6, 3), category_id=3, user_id=1),
    Expense(amount=1500, description="New shoes", date=datetime(2023, 6, 4), category_id=4, user_id=1),
    Expense(amount=3000, description="Doctor's appointment", date=datetime(2023, 6, 5), category_id=5, user_id=1),
    Expense(amount=800, description="Electricity bill", date=datetime(2023, 6, 6), category_id=6, user_id=1),
    Expense(amount=1200, description="Online course", date=datetime(2023, 6, 7), category_id=7, user_id=1),
    Expense(amount=5000, description="Rent", date=datetime(2023, 6, 8), category_id=8, user_id=1),
    Expense(amount=600, description="Miscellaneous expenses", date=datetime(2023, 6, 9), category_id=9, user_id=1)
]

budgets = [
    Budget(amount=2000, user_id=1, category_id=1),
    Budget(amount=1500, user_id=1, category_id=2),
    Budget(amount=1300, user_id=1, category_id=3),
    Budget(amount=2000, user_id=1, category_id=4),
    Budget(amount=4000, user_id=1, category_id=5),
    Budget(amount=1500, user_id=1, category_id=6),
    Budget(amount=2500, user_id=1, category_id=7),
    Budget(amount=8000, user_id=1, category_id=8),
    Budget(amount=1000, user_id=1, category_id=9)
]


session.add_all(categories)
session.add_all(expenses)
session.add_all(users)
session.add_all(budgets)

session.commit()

print("Database seeded successfully with initial data.")


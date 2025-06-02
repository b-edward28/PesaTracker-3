from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .user import User
from .base import Base
from .category import Category
from .expense import Expense
from .budget import Budget

engine = create_engine("sqlite:///pesatracker.db")
Session = sessionmaker(bind=engine)
session = Session()


print("Database initialized and tables created.")
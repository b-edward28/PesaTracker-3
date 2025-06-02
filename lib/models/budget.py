from sqlalchemy.orm import sessionmaker, relationship
from .base import Base
from .user import User
from .category import Category
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Budget(Base):
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    user = relationship('User', backref='budgets')
    category = relationship('Category', backref='budgets')  

    def __repr__(self):
        return (f"<Budget(id={self.id}, amount={self.amount}, "
                f"user_id={self.user_id}, category_id={self.category_id})>")
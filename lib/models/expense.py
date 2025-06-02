from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)


    user = relationship('User', backref='expenses')
    category = relationship('Category', backref='expenses')

    def __repr__(self):
        return (f"<Expense(id={self.id}, amount={self.amount}, "
                f"description='{self.description}', date={self.date}, "
                f"user_id={self.user_id}, category_id={self.category_id})>")

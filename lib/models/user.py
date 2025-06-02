from sqlalchemy import Column, Integer, String
from models import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

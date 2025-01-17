
from sqlalchemy import Column, DateTime, String, Integer, func 
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
metadata=Base.metadata

class Company(Base):
    __tablename__="company"

    id=Column(Integer, primary_key=True)
    name=Column(String(60), unique=True)
    created_at=Column(DateTime,default=func.now())
    address=Column(String(60), nullable=True)

    def __repr__(self):
        return f"id: {self.id} and name: {self.name}"
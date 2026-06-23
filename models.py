from sqlalchemy import Column, Integer, String, Float # Column is how we define a column in our table
from database import Base # we import Base from own database.py file . Base is the parent class

class Student(Base):  # This creates a python class called student by inheriting base
    __tablename__="students" #Sets the actual name of the table inside the database file

    id = Column(Integer, primary_key=True, index=True) # Unique identifier of the table. A column,integer
    name = Column(String, nullable=False)
    course = Column(String, nullable=False)
    grade = Column(Float, default= 0.0)  # It is a column and the datatype is float and defaults to 0.0 when no grade is passed 
    email = Column(String, unique=True)

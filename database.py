from sqlalchemy import create_engine   #create engine is a function that creates connections
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker #a fn that produces database sessions on demand

DATABASE_URL = "sqlite:///./grades.db"  #Tells the sqlalchemy where exactly our database lives. "/." means same folder

# The engine is the actual connection to the database, it uses URL to know where to connect
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})


#SessionLocal - blueprint for creatig sessions
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


# Base is the parent class for all our database models. class Student(base)
# Sqlalchemyknows studetn is a database table
Base = declarative_base()

def get_db():
    db = SessionLocal()  #Creates a fresh database session
    try:
        yield db #yield gives the session to whoever called get_db
    finally:
        db.close() #closes the sesion and returns the connection. Cleanup happens

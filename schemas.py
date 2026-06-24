from pydantic import BaseModel
from typing import Optional  # Have some fields being option

#what the user sends to CREATE
#StudentCreate - is the schema for when someone wants to add a new student
#(name, course, grade, email) - these are the fields they must send in their request

class StudentCreate(BaseModel):
    name:str
    course:str
    grade: float = 0.0
    email:str


# What the user sends to update
# StudentUpdate - is for when someone wants to change student details
# The key difference is here everything is optional. Why? Because whrn updating
# a user should send just one field and only change that
class StudentUpdate(BaseModel):
    name: Optional[str] = None # name is optional , if not sent, it is None(skip updating it)
    course: Optional[str] = None
    grade: Optional[float] = None

# What the API sends back 
# Student response is what comes back when someone makes a request
#- notice the student respomse includes id because after we create a student we want 
# to tell the user what ID they were assigned to)
class StudentResponse(BaseModel):
    id: int
    name: str
    course: str
    grade: float
    email: str

    # From_attributes = True its a bridge between database world and API WORLD
    # The database gives a SQLAlchemy object. The API needs to return a pydantic schema
    class Config: # Special class in pydantic (it holds a configuration settings)
        from_attributes = True # Without this line Pydantic cannot read SQLAlchemy

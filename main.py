# Where it all connects, It creates the fast api app
# creates the database tables
# Defines all the end points
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models,schemas,crud
from database import engine, get_db

# generate tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Grade Tracker", 
              description = "Track students gradeswith FastAPI",
              version = "1.0.0")

# Create 
@app.post("/students/", response_model = schemas.StudentResponse) #decorater tells FastApi when a post is sent run the function below
#response_model converts it to a student response shape(only the field defined in student response go out to the user)
def create_student(stuents: schemas.StudentCreate, db:Session = Depends(get_db)):
    #depends(get_db)- Its a dependency injection, it calls the get db fn and gets a session from it and passes it as db
    return crud.create_student(db,student) # Delegates to crud .pyie the end point does not touch the database

# Read all
@app.get("/students/",response_model = List[schemas.StudentResponse])
def get_students(db:Session = Depends(get_db)):
    return crud.get_students(db)

# Read one
@app.get("/students/{student_id}", response_model = schemas.StudentResponse)
def get_student(student_id: int, db:Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(404, "Student not found")
    return student

# Update
@app.put("/students/{student_id}", response_model = schemas. StudentResponse)
def update_student(student_id :int ,student:schemas.StudentUpdate, db:Session = Depends(get_db)):
    updated_student = crud.update_student(db,student_id, student)
    if not updated_student:
        raise HTTPException(404, "Student already recorded")
    return updated_student

# Delete 
@app.delete("/students/{student_id}", response_model = schemas. StudentResponse)
def delete_student(student_id:int, db:Session =Depends(get_db)):
    student = crud.delete_student(db,student_id)
    if not student:
        raise HTTPException(404, "Student already recorded")
    return {"message": "Student deleted successfully"}




        
         

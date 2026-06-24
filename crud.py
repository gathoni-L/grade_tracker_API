from sqlalchemy.orm import Session
import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.student(**student.model_dump())
    db.add(db_student) #Stage the record tells sql alchemy I want to have this
    db.commit() #Save to disk. This is when data is actually written to a database
    db.refresh(db_student)  # reloads the object  from database after saving(new id)
    return db_student #return completed student object


#Read one record
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


#Read all records
def get_student(db: Session, student_id: int):
    return db.query(models.Student).all()

# Update a record
def update_student(db: Session, student_id: int, data: schemas.StudentUpdate):
    student = db.query(models.Student).filter(models.Student.id == student_id).first() # Find the student you need to update
    if not student:  # If no student found return none
        return None
    updates = data.model_dump(exclude_unset=True) # It converts the update data to a dictionary 
    #eg if the user only sent grade, update will only contain grade
    # The for loop loops through each field and value that was sent
    for field, value in updates.items():
        setattr(student,field,value) #it sets an attribute on an object by name
        
    db.commit()
    db.refresh(student)
    return student

# Delete/remove a record
def delete_student(db:Session, student_id: int):
    # Find the student first. We cannot delete sth we have not found
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    # If not found return none
    if not student:  
        return None
    
    #Tells SQLAlchemy to delete the object
    db.delete(student)
    db.commit()
    return student

    



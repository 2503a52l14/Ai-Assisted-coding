# lab15_student_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Initialize the FastAPI app
app = FastAPI(
    title="Student Records API",
    description="A simple RESTful API for managing student records.",
    version="1.0.0"
)

# ----- Data Models -----
class Student(BaseModel):
    id: int
    name: str
    age: int
    major: str

# In-memory database (dictionary)
students_db = {}

# ----- API Endpoints -----

@app.get("/students", response_model=List[Student])
def get_students():
    """
    Get a list of all students.
    """
    return list(students_db.values())


@app.post("/students", response_model=Student)
def create_student(student: Student):
    """
    Add a new student to the database.
    """
    if student.id in students_db:
        raise HTTPException(status_code=400, detail="Student ID already exists.")
    students_db[student.id] = student
    return student


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_student: Student):
    """
    Update an existing student's details by ID.
    """
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found.")
    students_db[student_id] = updated_student
    return updated_student


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    """
    Delete a student record by ID.
    """
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found.")
    del students_db[student_id]
    return {"message": f"Student with ID {student_id} deleted successfully."}
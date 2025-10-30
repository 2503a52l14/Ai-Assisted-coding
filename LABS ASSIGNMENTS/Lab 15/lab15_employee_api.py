# lab15_employee_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict

app = FastAPI(
    title="Employee Payroll API",
    description="RESTful API to manage employees and their salaries.",
    version="1.0.0"
)

# ----- AI-Suggested Data Model -----
class Employee(BaseModel):
    """
    Represents an employee record with basic details and salary information.
    """
    id: int = Field(..., description="Unique employee ID")
    name: str = Field(..., description="Full name of the employee")
    department: str = Field(..., description="Department where the employee works")
    position: str = Field(..., description="Job title or role")
    salary: float = Field(..., description="Monthly salary of the employee")

class SalaryUpdate(BaseModel):
    """
    Represents the salary update structure for an existing employee.
    """
    salary: float = Field(..., description="Updated salary value")

# In-memory "database"
employees_db: Dict[int, Employee] = {}

# ----- API Endpoints -----

@app.get("/employees")
def list_employees():
    """
    Retrieve a list of all employees in the system.
    """
    return list(employees_db.values())


@app.post("/employees", response_model=Employee)
def add_employee(employee: Employee):
    """
    Add a new employee record, including salary details.
    """
    if employee.id in employees_db:
        raise HTTPException(status_code=400, detail="Employee ID already exists.")
    employees_db[employee.id] = employee
    return employee


@app.put("/employees/{employee_id}/salary", response_model=Employee)
def update_salary(employee_id: int, salary_update: SalaryUpdate):
    """
    Update the salary of an existing employee.
    """
    if employee_id not in employees_db:
        raise HTTPException(status_code=404, detail="Employee not found.")
    
    employee = employees_db[employee_id]
    employee.salary = salary_update.salary
    employees_db[employee_id] = employee
    return employee


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    """
    Remove an employee record from the system.
    """
    if employee_id not in employees_db:
        raise HTTPException(status_code=404, detail="Employee not found.")
    del employees_db[employee_id]
    return {"message": f"Employee with ID {employee_id} deleted successfully."}

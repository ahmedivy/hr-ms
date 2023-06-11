import csv
from datetime import datetime
from sqlmodel import select, Session

from core.database import engine
from models import Employee

# Function to parse the date in the specified format
def parse_date(date_string):
    return datetime.strptime(date_string, "%m/%d/%Y").date()

# Open the emps-mock.csv file and read the employee data
emp_file = "emp-mock.csv"
employees = []
with open(emp_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        employee = {
            "org_id": int(row["org_id"]),
            "emp_firstname": row["emp_firstname"],
            "emp_lastname": row["emp_lastname"],
            "emp_email": row["emp_email"],
            "emp_phone": row["emp_phone"],
            "emp_address": row["emp_address"],
            "emp_city": row["emp_city"],
            "emp_state": row["emp_state"],
            "emp_zip": row["emp_zip"],
            "emp_country": row["emp_country"],
            "emp_hire_date": parse_date(row["emp_hire_date"]),
            "emp_dob": parse_date(row["emp_dob"]),
            "emp_position": row["emp_position"],
            "emp_hourly_rate": float(row["emp_hourly_rate"])
        }
        employees.append(employee)

# Print the list of employees
for emp in employees:
    with Session(engine) as conn:
        emp = Employee(**emp)
        conn.add(emp)
        conn.commit()
        conn.refresh(emp)
        print(emp)

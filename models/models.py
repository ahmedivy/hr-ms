from typing import Optional, List
from datetime import date, datetime
from sqlmodel import SQLModel, Field, Relationship



class Organization(SQLModel, table=True):
    org_id: Optional[int] = Field(default=None, primary_key=True)
    org_name: str
    org_description: Optional[str] = None
    org_type: Optional[str] = None
    org_phone: str
    org_email: str
    org_website: Optional[str] = None
    org_logo_url: Optional[str] = None
    org_registration_date: datetime = Field(default=datetime.now())
    org_address: Optional[str] = None
    org_city: Optional[str] = None
    org_state: Optional[str] = None
    org_zip: Optional[str] = None
    org_country: Optional[str] = None

    employees: List["Employee"] = Relationship(back_populates="organization")

    __tablename__ = "organizations"

    class Config:
        orm_mode = True

class Employee(SQLModel, table=True):
    emp_id: Optional[int] = Field(default=None, primary_key=True)
    org_id: int = Field(default=None, foreign_key="organizations.org_id")
    emp_firstname: str
    emp_lastname: Optional[str] = None
    emp_cnic: str
    emp_email: str
    emp_phone: str
    emp_address: Optional[str] = None
    emp_city: Optional[str] = None
    emp_state: Optional[str] = None
    emp_zip: Optional[str] = None
    emp_country: Optional[str] = None
    emp_hire_date: date
    emp_termination_date: Optional[date] = Field(default=None)
    emp_dob: date
    emp_position: str
    emp_hourly_rate: int

    organization: Optional[Organization] = Relationship(back_populates="employees")

    __tablename__ = "employees"

    class Config:
        orm_mode = True


class Loan(SQLModel, table=True):
    loan_id: Optional[int] = Field(default=None, primary_key=True)
    emp_id: int = Field(default=None, foreign_key="employees.emp_id")
    loan_amount: float
    loan_date: datetime
    loan_status: str
    loan_description: str

    __tablename__ = "loans"

    class Config:
        orm_mode = True


class Salary(SQLModel, table=True):
    sal_id: Optional[int] = Field(default=None, primary_key=True)
    org_id: int = Field(default=None, foreign_key="organizations.org_id")
    sal_created_date: date
    sal_month: str
    sal_year: str
    sal_discription: Optional[str] = None

    __tablename__ = "salaries"

    class Config:
        orm_mode = True


class SalaryDetail(SQLModel, table=True):
    sal_id: int = Field(default=None, foreign_key="salaries.sal_id", primary_key=True)
    emp_id: int = Field(default=None, foreign_key="employees.emp_id", primary_key=True)
    sal_gross_amount: float
    sal_deductions: float
    sal_net_amount: float

    __tablename__ = "salaryDetails"

    class Config:
        orm_mode = True


class Attendance(SQLModel, table=True):
    atd_id: Optional[int] = Field(default=None, primary_key=True)
    org_id: int = Field(default=None, foreign_key="organizations.org_id")
    atd_date: date

    __tablename__ = "attendances"

    class Config:
        orm_mode = True


class AttendanceDetail(SQLModel, table=True):
    atd_id: int = Field(default=None, foreign_key="attendances.atd_id", primary_key=True)
    emp_id: int = Field(default=None, foreign_key="employees.emp_id", primary_key=True)
    atd_start_time: datetime
    atd_end_time: datetime

    __tablename__ = "attendanceDetails"

    class Config:
        orm_mode = True

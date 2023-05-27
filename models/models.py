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

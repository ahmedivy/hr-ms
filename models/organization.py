from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field


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

    __tablename__ = "organizations"

    class Config:
        orm_mode = True

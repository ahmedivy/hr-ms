import csv
from datetime import datetime
from sqlmodel import select, Session

from core.database import engine

from models import Organization
# Function to parse the date in the specified format
def parse_date(date_string):
    return datetime.strptime(date_string, "%m/%d/%Y").date()

# Open the org.csv file and read the data
org_file = "orgs.csv"
organizations = []
with open(org_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        organizations.append(row)

# Open the org-mock.csv file and update the organization dictionaries
org_mock_file = "orgs-mock.csv"
with open(org_mock_file, "r") as file:
    reader = csv.DictReader(file)
    for i, row in enumerate(reader):
        if i < len(organizations):
            organizations[i]["org_name"] = row["org_name"]
            organizations[i]["org_description"] = row["org_description"]
            organizations[i]["org_type"] = row["org_type"]
            organizations[i]["org_phone"] = row["org_phone"]
            # organizations[i]["org_email"] = row["org_email"]
            # organizations[i]["org_website"] = row["org_website"]
            organizations[i]["org_logo_url"] = row["org_logo_url"]
            organizations[i]["org_registration_date"] = parse_date(row["org_registration_date"])
            organizations[i]["org_address"] = row["org_address"]
            organizations[i]["org_city"] = row["org_city"]
            organizations[i]["org_state"] = row["org_state"]
            organizations[i]["org_zip"] = row["org_zip"]
            organizations[i]["org_country"] = row["org_country"]

# Print the list of organizations
with Session(engine) as conn:
    for org in organizations:
        org = Organization(**org)
        conn.add(org)
        conn.commit()
        conn.refresh(org)
        print(org)
    
        
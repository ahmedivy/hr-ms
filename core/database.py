from sqlmodel import create_engine

from .configs import Settings

cxn_str = f"mssql+pyodbc://{Settings.DB_SERVER}/{Settings.DB_NAME}?driver={Settings.DB_DRIVER}"
engine = create_engine(cxn_str, echo=False)

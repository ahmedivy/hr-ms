from sqlmodel import create_engine
from pyodbc import connect

from .configs import Settings

cxn_str = f"mssql+pyodbc://{Settings.DB_SERVER}/{Settings.DB_NAME}?driver={Settings.DB_DRIVER}"

pd_cxn_str = f"DRIVER={Settings.DB_DRIVER};SERVER={Settings.DB_SERVER};DATABASE={Settings.DB_NAME};Trusted_Connection=yes;"
pd_connection = connect(pd_cxn_str)
cursor = pd_connection.cursor()

engine = create_engine(cxn_str, echo=False)

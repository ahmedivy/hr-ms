from pyodbc import connect

from .configs import Settings

cxn_str = f"DRIVER={Settings.DB_DRIVER};SERVER={Settings.DB_SERVER};DATABASE={Settings.DB_NAME};Trusted_Connection=yes;"

connection = connect(cxn_str)

cursor = connection.cursor()

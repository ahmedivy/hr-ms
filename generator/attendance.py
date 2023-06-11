import pyodbc

pd_cxn_str = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER=HP-NOTEBOOK;DATABASE=hr-ms;Trusted_Connection=yes;"

pd_cxn = pyodbc.connect(pd_cxn_str)
cursor = pd_cxn.cursor()

stmt = "select org_id, org_name from organizations"

cursor.execute(stmt)
orgs = cursor.fetchall()

emps = {}

for id, name in orgs:
    stmt = f"select emp_id from employees where org_id = {id}"
    cursor.execute(stmt)
    emps[id] = cursor.fetchall()
    
print(len(emps[106]))
    
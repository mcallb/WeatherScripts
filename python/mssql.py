import pymssql 
conn = pymssql.connect(host='srv-sql', user='pyodbc', password='pyodbc', database='master') 
cur = conn.cursor() 

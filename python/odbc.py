#!/usr/bin/python
import pyodbc
#connection = pyodbc.connect("DRIVER={freeTDS};SERVER=srv-sql;DATABASE=master;UID=pyodbc;PWD=pyodbc")
connection = pyodbc.connect("DRIVER={SQL Server};SERVER=srv-sql;DATABASE=master;UID=pyodbc;PWD=pyodbc")
#then to call the database just use a cursor
cur = connection.cursor()
cur.execute("SELECT name FROM sys.syslogins")
for row in cur:
	print "NAME: %s"% row.name

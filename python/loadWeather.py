#!/usr/bin/env python
import time
import ow
#import pyodbc
# Read the owfs devices
ow.init('localhost:3001')
ow.error_level(ow.error_level.fatal)
ow.error_print(ow.error_print.stderr)
temp = ow._get("10.56217F010800/temperature")
time = time.strftime("%Y-%m-%d %H:%M:%S")
print time, temp
#connection = pyodbc.connect("DRIVER={SQL Server};SERVER=srv-sql;DATABASE=master;UID=pyodbc;PWD=pyodbc")
#Sensor("/")

# If connection fails call some error handling
# then to call the database just use a cursor
#cur = connection.cursor()
#cur.execute("SELECT name FROM sys.syslogins")
#for row in cur:
#	print "NAME: %s"% row.name



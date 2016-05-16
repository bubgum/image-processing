#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","zosso","citra" )
cursor = db.cursor()

sql = "SELECT file_name FROM upload WHERE id=(SELECT MAX(id) FROM upload);"
cursor.execute(sql)
row = cursor.fetchone()
while row is not None:
    path = 'C:/Ampps/www/citra/uploads/' + str(row)[3:-3]    
    row = cursor.fetchone()
  

print path

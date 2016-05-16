#from mysql.connector import MySQLConnection, Error
#from python_mysql_dbconfig import read_db_config
 
#def insert_data(daftar):
#    query = "INSERT INTO citra(img_source,fitur_0,fitur_1,fitur_2,fitur_3,fitur_4,fitur_5,fitur_6,fitur_7,fitur_8,fitur_9,fitur_10,fitur_11,fitur_12,fitur_13,fitur_14,fitur_15,fitur_16,fitur_17,fitur_18,fitur_19,fitur_20,fitur_21,fitur_22,fitur_23,fitur_24,fitur_25,fitur_26,fitur_27,fitur_28,fitur_29,fitur_30,fitur_31,fitur_32,fitur_33,fitur_34,fitur_35,fitur_36,fitur_37,fitur_38,fitur_39,fitur_40,fitur_41,fitur_42,fitur_43,fitur_44,fitur_45,fitur_46,fitur_47,fitur_48,fitur_49,fitur_50,fitur_51,fitur_52,fitur_53,fitur_54,fitur_55,fitur_56,fitur_57,fitur_58,fitur_59,fitur_60,fitur_61,fitur_62,fitur_63,fitur_64,fitur_65,fitur_66,fitur_67,fitur_68,fitur_69,fitur_70,fitur_71,fitur_72,fitur_73,fitur_74,fitur_75,fitur_76,fitur_77,fitur_78,fitur_79,fitur_80,fitur_81) " \
#            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# 
#    try:
#        db_config = read_db_config()
#        conn = MySQLConnection(**db_config)
# 
#        cursor = conn.cursor()
#        cursor.executemany(query, daftar)
# 
#        conn.commit()
#    except Error as e:
#        print('Error:', e)
# 
#    finally:
#        cursor.close()
#        conn.close()
# 
#def main():
#
#    daftar = [('tes.jpg',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81)]
#    insert_data(daftar)
# 
#if __name__ == '__main__':
#    main()

#def insert_data(daftar):
#    query = "INSERT INTO coba(nama,umur,hobi) " \
#            "VALUES(%s,%s,%s)"
# 
#    try:
#        db_config = read_db_config()
#        conn = MySQLConnection(**db_config)
# 
#        cursor = conn.cursor()
#        cursor.executemany(query, daftar)
# 
#        conn.commit()
#    except Error as e:
#        print('Error:', e)
# 
#    finally:
#        cursor.close()
#        conn.close()
# 
#def main():
#    daftar = [('Ali',13,'bimbingan')]
#    insert_data(daftar)
# 
#if __name__ == '__main__':
#    main()
    
###############################################################################
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","zosso","citra" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO coba(nama,umur,hobi) \
       VALUES ('%s','%s','%s')" % ('Aripo',40,'boker')

print sql

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()


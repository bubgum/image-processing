# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 20:25:58 2016

@author: bubgum
"""
import matplotlib.pyplot as plt
from mysql.connector import MySQLConnection, Error
import MySQLdb

def distance():
    try:
        db = MySQLdb.connect("localhost","root","zosso","citra" )
        cursor = db.cursor()
        cursor.execute("DELETE FROM canbera_canny")
        db.commit()
        

        db = MySQLdb.connect("localhost","root","zosso","citra" )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM data_train_canny")
        data_train =  list(cursor)
            
        cursor = db.cursor()
        cursor.execute("SELECT * FROM data_test_canny WHERE no=(SELECT MAX(no) FROM data_test_canny);")
        data_test = list(cursor)       
        
        
        index1 = 0
        for x in range(len(data_train)) :
        
            canbera = 0
            index2 = 2
            
            for y in range(82):                
                temp1 = (data_test[0][index2] - data_train[index1][index2]) 
                temp2 = (data_test[0][index2] + data_train[index1][index2])
                                
                if temp2 == 0 :
                    hasil_temp = abs(temp1)
                else :
                    hasil_temp = float(abs(temp1)) / float(temp2)
                
                canbera = float(canbera) + float(hasil_temp)
                print canbera
                index2 += 1
            query = "INSERT INTO canbera_canny \
                    VALUES (%s, %s, %d) " % (data_test[0][0], data_train[index1][0], canbera)
            db = MySQLdb.connect("localhost","root","zosso","citra" )
    
            cursor = db.cursor()
            cursor.execute(query)
     
            db.commit()
            index1+=1
#            print canbera
            
        db = MySQLdb.connect("localhost","root","zosso","citra" )    
        cursor = db.cursor()
        
        sql = "SELECT canbera_canny.result, data_train_canny.img_source FROM canbera_canny JOIN data_train_canny ON canbera_canny.id_train = data_train_canny.no ORDER BY canbera_canny.result ASC LIMIT 10"
        cursor.execute(sql)
        row = list(cursor)
        index=0
        for x in range(len(row)) :
#            row = cursor.fetchone()
            img = row[index][1]
            print img
            index+=1
#            query = "INSERT INTO result \
#                    VALUES (%d,'%s') " % ('',row[index][1])
#            index+=1
#            db = MySQLdb.connect("localhost","root","zosso","citra" )
#    
#            cursor = db.cursor()
#            cursor.execute(query)        
            db.commit()
            
        
        
#       plt.subplot(241),plt.imshow(img),plt.title('Gambar Asli')
#        plt.subplot(242),plt.hist(sudut0),plt.title('sudut0')
#        plt.subplot(243),plt.hist(sudut90),plt.title('sudut90')
#        plt.subplot(244),plt.hist(sudut45),plt.title('sudut45')
#        plt.subplot(245),plt.hist(sudut135),plt.title('sudut135')

    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        db.close()

if __name__ == '__main__':
    distance()
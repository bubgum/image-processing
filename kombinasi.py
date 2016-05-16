# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:13:56 2016

@author: bubgum
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

# VARS
maksWarna = 64
file = 'E:/py/BatikTrain/B1_5.jpg' 
channel = 'blue'

imgSource = cv2.imread(file)
destRGB = cv2.cvtColor(imgSource, cv2.COLOR_BGR2RGB)

height, width, channel = destRGB.shape
red, green, blue = cv2.split(destRGB)
bins = 256 / maksWarna

# Quantisation process
for x in range(height):
    for y in range(width):
        red[x][y]  = red[x][y]  * bins / 256
        green[x][y] = green[x][y] * bins / 256
        blue[x][y]   = blue[x][y]   * bins / 256

imgKuantisasi = cv2.imread(file,cv2.CV_8U)
 
for x in range(height):
    for y in range(width):       
        imgKuantisasi[x][y] = ((bins * bins * red[x][y]) + (bins + green[x][y]) + blue[x][y])       

# generate empty array               
textonUH = []
textonLH = []
textonVL = []
textonVR = []
textonDL = []
textonDR = []
combinedTextonWarna = []

# generate array index depend on color counter
for arr in range(maksWarna):
    textonUH.append(0) 
    textonLH.append(0)
    textonVL.append(0)
    textonVR.append(0)
    textonDL.append(0)
    textonDR.append(0)
    combinedTextonWarna.append(0)
# compare and counting maxton matching templates and put it inside defined array
for x in range(height-1):
    for y in range(width-1):
        # Upper Horizontal
        if((imgKuantisasi[x,y]) == (imgKuantisasi[x,y+1])):
            textonUH[imgKuantisasi[x,y]-1] += 1
        # Lower Horizontal
        if((imgKuantisasi[x+1,y]) == (imgKuantisasi[x+1,y+1])):
            textonLH[imgKuantisasi[x,y]-1] += 1   
        # Vertical Left
        if((imgKuantisasi[x,y]) == (imgKuantisasi[x+1,y])):
            textonVL[imgKuantisasi[x,y]-1] += 1     
        # Vertical Right
        if((imgKuantisasi[x,y+1]) == (imgKuantisasi[x+1,y+1])):
            textonVR[imgKuantisasi[x,y]-1] += 1  
        # Diagonal Top on Left
        if((imgKuantisasi[x,y]) == (imgKuantisasi[x+1,y+1])):
            textonDL[imgKuantisasi[x,y]-1] += 1     
        # Diagonal Top on Right
        if((imgKuantisasi[x,y+1]) == (imgKuantisasi[x+1,y])):
            textonDR[imgKuantisasi[x,y]-1] += 1    

for x in range(maksWarna):
    combinedTextonWarna[x] = (textonUH[x] + textonLH[x] + textonVL[x] + textonVR[x] + textonDL[x] + textonDR[x]) / 6


#############################################################################################

img = cv2.imread(file, 0)

laplacian = cv2.Laplacian(img,cv2.CV_8U)

#plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
#plt.title('Original')
#plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
#plt.title('Laplacian')
#plt.show()

maksWarna = 18
imgSource = cv2.imread(file)
height, width, channel = imgSource.shape
bins = 256 / maksWarna

# Quantisation process
for x in range(height ):
    for y in range(width):
        laplacian[x][y] = laplacian[x][y] * bins / 256

# generate empty array               
textonUH = []
textonLH = []
textonVL = []
textonVR = []
textonDL = []
textonDR = []
combinedTextonSobel = []

#generate array index depend on color counter
for arr in range(maksWarna):
    textonUH.append(0)
    textonLH.append(0)
    textonVL.append(0)
    textonVR.append(0)
    textonDL.append(0)
    textonDR.append(0)
    combinedTextonSobel.append(0)
# compare and counting maxton matching templates and put it inside defined array
for x in range(height-1):
    for y in range(width-1):
        # Upper Horizontal
        if((laplacian[x,y]) == (laplacian[x,y+1])):
            textonUH[laplacian[x,y]-1] += 1
        # Lower Horizontal
        if((laplacian[x+1,y]) == (laplacian[x+1,y+1])):
            textonLH[laplacian[x,y]-1] += 1   
        # Vertical Left
        if((laplacian[x,y]) == (laplacian[x+1,y])):
            textonVL[laplacian[x,y]-1] += 1     
        # Vertical Right
        if((laplacian[x,y+1]) == (laplacian[x+1,y+1])):
            textonVR[laplacian[x,y]-1] += 1  
        # Diagonal Top on Left
        if((laplacian[x,y]) == (laplacian[x+1,y+1])):
            textonDL[laplacian[x,y]-1] += 1     
        # Diagonal Top on Right
        if((laplacian[x,y+1]) == (laplacian[x+1,y])):
            textonDR[laplacian[x,y]-1] += 1  

for x in range(maksWarna):
    combinedTextonSobel[x] = (textonUH[x] + textonLH[x] + textonVL[x] + textonVR[x] + textonDL[x] + textonDR[x]) / 6

gabungan =  combinedTextonWarna + combinedTextonSobel

#for x in range(len(gabungan)):
#    print 'nilai array ke ', x , ' : ', gabungan[x]
#    

    
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

    
def input_data():

    for x in range(len(gabungan)):
        gabungan[x]

    query = "INSERT INTO data_test " 
    nilai = "VALUES (\"\"," + "\"" + file + "\"" + ","
    for x in range(len(gabungan)):
        nilai = nilai + str(gabungan[x])
        if x < len(gabungan)-1 :
            nilai = nilai + ", " 
            
    query = query + nilai + ")"
#    print query
        
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query)
 
        conn.commit()
    except Error as e:
        print('Error:', e)
 
    finally:
        cursor.close()
        conn.close() 

def search():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data_train")
        #row_train = cursor.fetchone()
        data_train =  list(cursor)
            
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data_test")
        data_test = list(cursor)
        
        
        index1 = 0
        for x in range(len(data_train)) :
        
            canbera = 0
            index2 = 2
            
            for y in range(82):                
                temp1 = (data_test[0][index2] - data_train[index1][index2]) 
                temp2 = (data_test[0][index2] + data_train[index1][index2])

                #print "temp1 "+str(temp1)
                #print "temp2 "+str(temp2)
                                
                if temp2 == 0 :
                    hasil_temp = abs(temp1)
                else :
                    hasil_temp = float(abs(temp1)) / float(temp2)
                
                #print "hasil temp = " + str(hasil_temp)
                canbera = float(canbera) + float(hasil_temp)
                
                index2 += 1
            index1+=1
            
            print canbera
        
            
        #for x in range(len(gabungan)):
            #row_train[x]
        
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
        
    
    
        
 
if __name__ == '__main__':
#    input_data()
    search()




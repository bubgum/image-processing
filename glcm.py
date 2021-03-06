# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:13:56 2016

@author: bubgum
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math


file = 'E:/py/BatikTest/B43_1.jpg' 

# baca resource gambar
imgSource = cv2.imread(file)
gray = cv2.cvtColor(imgSource, cv2.COLOR_BGR2GRAY)
height, width, channel = imgSource.shape

# generate empty array               
sudut0 = []
sudut90 = []
sudut135 = []
sudut45 = []
norm0 = []
norm45 = []
norm90 = []
norm135 = []
theta0 = []
theta45 = []
theta90 = []
theta135 = []
img0 = []
img45 = []
img90 = []
img135 = []
co = []
co0 = []
co45 = []
co90 = []
co135 = []
entr0 = []
entr45 = []
entr90 = []
entr135 = []
ver = [[0]*128 for i in range(128)]
cor = [[0]*128 for i in range(128)]
corre0 = []
corre45 = []
corre90 = []
corre135 = []
combinedGlcm = []

# generate array index depend on color counter
for arr in range(255):
    sudut0.append(0) 
    sudut90.append(0)
    sudut135.append(0)
    sudut45.append(0)
    norm0.append(0)
    norm45.append(0)
    norm90.append(0)
    norm135.append(0)
    theta0.append(0)
    theta45.append(0)
    theta90.append(0)
    theta135.append(0)
    img0.append(0)
    img45.append(0)
    img90.append(0)
    img135.append(0)
    co.append(0)
    co0.append(0)
    co45.append(0)
    co90.append(0)
    co135.append(0)  
    entr0.append(0)
    entr45.append(0)
    entr90.append(0)
    entr135.append(0)
    corre0.append(0)
    corre45.append(0)
    corre90.append(0)
    corre135.append(0)
    #combinedGlcm.append(0)
    
# compare and counting maxton matching templates and put it inside defined array
for x in range(height-1):
    for y in range(width-1):
        # 0
        if((gray[x,y]) == (gray[x,y+1])):
            sudut0[gray[x,y]-1] += 1
        # 90
        if((gray[x,y]) == (gray[x+1,y])):
            sudut90[gray[x,y]-1] += 1      
        # 135
        if((gray[x,y]) == (gray[x+1,y+1])):
            sudut135[gray[x,y]-1] += 1     
        # 45
        if((gray[x,y+1]) == (gray[x+1,y])):
            sudut45[gray[x,y]-1] += 1 
            
#jumlah piksel
sum_pixels0 = sum(sudut0)
sum_pixels45 = sum(sudut45)
sum_pixels90 = sum(sudut90)
sum_pixels135 = sum(sudut135)

#normalisasi
for x in range(len(sudut0)):
    norm0[x] = float(sudut0[x]) / float(sum_pixels0)
    norm45[x] = float(sudut45[x]) / float(sum_pixels45)
    norm90[x] = float(sudut90[x]) / float(sum_pixels90)
    norm135[x] = float(sudut135[x]) / float(sum_pixels135)
    
#energy per theta
for x in range(len(sudut0)):
    theta0[x] = pow(norm0[x],2)
    sum_tetha0 = sum(theta0)
    theta45[x] = pow(norm45[x],2)
    sum_tetha45 = sum(theta45)
    theta90[x] = pow(norm90[x],2)
    sum_tetha90 = sum(theta90)
    theta135[x] = pow(norm135[x],2)
    sum_tetha135 = sum(theta135)
    
#co-occ
for x in range(len(sudut0)):
    co[x] = float(norm0[x]) + float(norm45[x]) + float(norm90[x]) + float(norm135[x])
    

#energy per image
for x in range(len(sudut0)):
    img0[x] = pow(norm0[x],2)
    sum_enr0 = sum(img0)
    img45[x] = pow(norm45[x],2)
    sum_enr45 = sum(img45)
    img90[x] = pow(norm90[x],2)
    sum_enr90 = sum(img90)
    img135[x] = pow(norm135[x],2)
    sum_enr135 = sum(img135)

#contrast

for x in range(height):
    for y in range(width):
        ver[x][y] =  pow(x-y,2) 

for x in range(height):
    co0[x] = ver[x][y] * norm0[x]
    sum_con0 = sum(co0)
    co45[x] = ver[x][y] * norm45[x]
    sum_con45 = sum(co45)
    co90[x] = ver[x][y] * norm90[x]
    sum_con90 = sum(co90)
    co135[x] = ver[x][y] * norm135[x]
    sum_con135 = sum(co135)

#correlation

for x in range(height):
    for y in range(width):
        cor[x][y] =  x * y 

for x in range(height):
    corre0[x] = cor[x][y] * norm0[x]
    sum_corre0 = sum(corre0)
    corre45[x] = cor[x][y] * norm45[x]
    sum_corre45 = sum(corre45)
    corre90[x] = cor[x][y] * norm90[x]
    sum_corre90 = sum(corre90)
    corre135[x] = cor[x][y] * norm135[x]
    sum_corre135 = sum(corre135)


#entropy
for x in range (len(sudut0)):
    if (norm0[x] == 0 or norm45[x] == 0 or norm90[x] == 0 or norm135[x] == 0):
        entr0[x] = 0
        entr45[x] = 0
        entr90[x] = 0
        entr135[x] = 0
    else :
        entr0[x] = abs(norm0[x] * (math.log(norm0[x], 2)))
        sum_entropy0 = sum(entr0)
        entr45[x] = abs(norm45[x] * (math.log(norm45[x], 2)))
        sum_entropy45 = sum(entr45)
        entr90[x] = abs(norm90[x] * (math.log(norm90[x], 2)))
        sum_entropy90 = sum(entr90)
        entr135[x] = abs(norm135[x] * (math.log(norm135[x], 2)))
        sum_entropy135 = sum(entr135)
    
combinedEnergy = sum_enr0, sum_enr45, sum_enr90, sum_enr135
combinedContrast = sum_con0, sum_con45, sum_con90, sum_con135
combinedCorrelation = sum_corre0, sum_corre45, sum_corre90, sum_corre135
combinedEntropy = sum_entropy0, sum_entropy45, sum_entropy90, sum_entropy135

combinedGlcm = combinedEnergy + combinedContrast + combinedCorrelation + combinedEntropy
glcm = list(combinedGlcm)    
print glcm


        
plt.subplot(241),plt.imshow(gray),plt.title('Grayscale')
plt.subplot(242),plt.hist(combinedGlcm),plt.title('Combined')
plt.subplot(243),plt.hist(combinedEnergy),plt.title('Energy')
plt.subplot(245),plt.hist(combinedContrast),plt.title('Contrast')
plt.subplot(246),plt.hist(combinedCorrelation),plt.title('Correlation')
plt.subplot(247),plt.hist(combinedEntropy),plt.title('Entropy')




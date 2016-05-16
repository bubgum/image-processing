# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:12:00 2016

@author: bubgum
"""
import cv2
import numpy as np

import cv2
import numpy as np
from matplotlib import pyplot as plt

file = 'E:/py/BatikTest/B43_1.jpg'
imgSource = cv2.imread(file) 
img = cv2.imread(file, 0)
destRGB = cv2.cvtColor(imgSource, cv2.COLOR_BGR2RGB)
laplacian = cv2.Canny(img,100,200)
#laplacian = cv2.Sobel(img,0,0,1)

#plt.subplot(241),plt.imshow(destRGB,cmap = 'gray')
#plt.title('Original')
#plt.subplot(242),plt.imshow(laplacian,cmap = 'gray')
#plt.title('Laplacian')
#plt.show()

maksWarna = 18
# baca resource gambar
imgSource = cv2.imread(file)
# baca header gambar dan ambil tinggi, lebar dan jumlah channel
height, width, channel = imgSource.shape

# jumlah warna kuantisasi
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
combinedTexton = []

#generate array index depend on color counter
for arr in range(maksWarna):
    textonUH.append(0)
    textonLH.append(0)
    textonVL.append(0)
    textonVR.append(0)
    textonDL.append(0)
    textonDR.append(0)
    combinedTexton.append(0)
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
    combinedTexton[x] = (textonUH[x] + textonLH[x] + textonVL[x] + textonVR[x] + textonDL[x] + textonDR[x]) / 6

plt.subplot(241),plt.imshow(laplacian,cmap = 'gray'),plt.title('Laplacian')
plt.subplot(242),plt.imshow(destRGB),plt.title('Gambar Asli')
plt.subplot(243),plt.hist(textonUH),plt.title('textonUH')
plt.subplot(244),plt.hist(textonLH),plt.title('textonLH')
plt.subplot(245),plt.hist(textonVL),plt.title('textonVL')
plt.subplot(246),plt.hist(textonVR),plt.title('textonVR')
plt.subplot(247),plt.hist(textonDL),plt.title('textonDL')
plt.subplot(248),plt.hist(textonDR),plt.title('textonDR')

plt.show()

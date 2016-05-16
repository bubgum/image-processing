# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:13:56 2016

@author: bubgum
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# VARS
maksWarna = 64
file = 'E:/py/BatikTest/B43_1.jpg' 
channel = 'blue'

# baca resource gambar
imgSource = cv2.imread(file)

# baca header gambar dan ambil tinggi, lebar dan jumlah channel
height, width, channel = imgSource.shape
# pisahkan channel menjadi RGB
blue, green, red = cv2.split(imgSource)
# jumlah warna kuantisasi
bins = 256 / maksWarna

# Quantisation process
for x in range(height):
    for y in range(width):
        blue[x][y]  = blue[x][y]  * bins / 256
        green[x][y] = green[x][y] * bins / 256
        red[x][y]   = red[x][y]   * bins / 256

#imgKuantisasi = red
#combinedTexton = imgKuantisasi
#imgKuantisasi = red

imgKuantisasi = cv2.imread(file,cv2.CV_8U)
 
for x in range(height):
    for y in range(width):       
        imgKuantisasi[x][y] = ((bins * bins * red[x][y]) + (bins + green[x][y]) + blue[x][y])       



## generate empty array               
textonUH = []
textonLH = []
textonVL = []
textonVR = []
textonDL = []
textonDR = []
combinedTexton = []

# generate array index depend on color counter
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
    combinedTexton[x] = (textonUH[x] + textonLH[x] + textonVL[x] + textonVR[x] + textonDL[x] + textonDR[x]) / 6

##combinedTexton = np.sum([textonUH, textonLH, textonVL, textonVR, textonDL, textonDR], axis=0)
##combinedTexton = (textonUH[imgKuantisasi[x,y]] + textonLH[imgKuantisasi[x,y]] + textonVL[imgKuantisasi[x,y]] + textonVR[imgKuantisasi[x,y]] + textonDL[imgKuantisasi[x,y]] + textonDR[imgKuantisasi[x,y]]) / 6
#
#plt.subplot(242),plt.imshow(imgSource),plt.title('Gambar Asli')
##plt.subplot(242),plt.imshow(imgKuantisasi,'gray'),plt.title('Kuantisasi bin=4')
#
plt.subplot(243),plt.hist(textonUH),plt.title('textonUH')
plt.subplot(244),plt.hist(textonLH),plt.title('textonLH')
plt.subplot(245),plt.hist(textonVL),plt.title('textonVL')
plt.subplot(246),plt.hist(textonVR),plt.title('textonVR')
plt.subplot(247),plt.hist(textonDL),plt.title('textonDL')
plt.subplot(248),plt.hist(textonDR),plt.title('textonDR')
plt.subplot(241),plt.hist(combinedTexton),plt.title('combinedTexton')
#



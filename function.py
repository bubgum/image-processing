# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 01:08:22 2016

@author: bubgum
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

class function :

    global maksWarna
#    maksWarna = 18
    file = 'E:/py/BatikTest/B43_1.jpg' 
    channel = 'blue'
    global bins, imgSource
#    bins = 256 / maksWarna
    imgSource = cv2.imread(file)
    global height, width, channel
    height, width, channel = imgSource.shape
    global blue, green, red
    blue, green, red = cv2.split(imgSource)
    global imgKuantisasi
    imgKuantisasi = cv2.imread(file,cv2.CV_8U)
    global textonUH, textonLH, textonVL, textonVR, textonDL, textonDR, combinedTexton
    
    #generate empty array               
    textonUH = []
    textonLH = []
    textonVL = []
    textonVR = []
    textonDL = []
    textonDR = []
    combinedTexton = []
    
    #generate array index depend on color counter
    def inTex(self,maksWarna):
        for arr in range(maksWarna):
            textonUH.append(0) 
            textonLH.append(0)
            textonVL.append(0)
            textonVR.append(0)
            textonDL.append(0)
            textonDR.append(0)
            combinedTexton.append(0)
    
    def deteksiTexton(self,objValue):
        for x in range(height-1):
            for y in range(width-1):
                # Upper Horizontal
                if((objValue[x,y]) == (objValue[x,y+1])):
                    textonUH[objValue[x,y]-1] += 1
                # Lower Horizontal
                if((objValue[x+1,y]) == (objValue[x+1,y+1])):
                    textonLH[objValue[x,y]-1] += 1   
                # Vertical Left
                if((objValue[x,y]) == (objValue[x+1,y])):
                    textonVL[objValue[x,y]-1] += 1     
                # Vertical Right
                if((objValue[x,y+1]) == (objValue[x+1,y+1])):
                    textonVR[objValue[x,y]-1] += 1  
                # Diagonal Top on Left
                if((objValue[x,y]) == (objValue[x+1,y+1])):
                    textonDL[objValue[x,y]-1] += 1     
                # Diagonal Top on Right
                if((objValue[x,y+1]) == (objValue[x+1,y])):
                    textonDR[objValue[x,y]-1] += 1 
    
    def textonCombined(self,uh,lh,vl,vr,dl,dr,maksWarna):
        for x in range(maksWarna):
            combinedTexton[x] = (uh[x] + lh[x] + vl[x] + vr[x] + dl[x] + dr[x]) / 6
            
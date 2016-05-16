# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 23:59:49 2016

@author: bubgum
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from function import *


class classfiturwarna:
    
    global maksWarna    
    maksWarna = 64
    bins = 256 / maksWarna
    
    func = function()
    
    for x in range(height):
        for y in range(width):
            blue[x][y]  = blue[x][y]  * bins / 256
            green[x][y] = green[x][y] * bins / 256
            red[x][y]   = red[x][y]   * bins / 256
     
    for x in range(height):
        for y in range(width):       
            imgKuantisasi[x][y] = ((bins * bins * red[x][y]) + (bins + green[x][y]) + blue[x][y])       
       
    func.inTex(maksWarna)
    func.deteksiTexton(imgKuantisasi)
    func.textonCombined(textonUH,textonLH,textonVL,textonVR,textonDL,textonDR,maksWarna)
            
#    plt.subplot(242),plt.imshow(imgSource),plt.title('Gambar Asli')
#    plt.subplot(243),plt.hist(textonUH),plt.title('textonUH')
#    plt.subplot(244),plt.hist(textonLH),plt.title('textonLH')
#    plt.subplot(245),plt.hist(textonVL),plt.title('textonVL')
#    plt.subplot(246),plt.hist(textonVR),plt.title('textonVR')
#    plt.subplot(247),plt.hist(textonDL),plt.title('textonDL')
#    plt.subplot(248),plt.hist(textonDR),plt.title('textonDR')
#    plt.subplot(241),plt.hist(combinedTexton),plt.title('combinedTexton')

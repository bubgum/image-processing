# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:12:00 2016

@author: bubgum
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from function import *

class classsobel:
    
    maksWarna = 18
    bins = 256 / maksWarna    
    
    func = function()
    
    file = 'E:/py/BatikTest/B43_1.jpg' 
    img = cv2.imread(file, 0)
    
    laplacian = cv2.Laplacian(img,cv2.CV_8U)
    
    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original')
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian')
    plt.show()

    
    # Quantisation process
    for x in range(height ):
        for y in range(width):
            laplacian[x][y] = laplacian[x][y] * bins / 256

    func.inTex(maksWarna)        
    func.deteksiTexton(laplacian)
    func.textonCombined(textonUH,textonLH,textonVL,textonVR,textonDL,textonDR,maksWarna)
        
#    plt.subplot(243),plt.hist(textonUH),plt.title('textonUH')
#    plt.subplot(244),plt.hist(textonLH),plt.title('textonLH')
#    plt.subplot(245),plt.hist(textonVL),plt.title('textonVL')
#    plt.subplot(246),plt.hist(textonVR),plt.title('textonVR')
#    plt.subplot(247),plt.hist(textonDL),plt.title('textonDL')
#    plt.subplot(248),plt.hist(textonDR),plt.title('textonDR')
#    plt.subplot(241),plt.hist(combinedTexton),plt.title('combinedTexton')

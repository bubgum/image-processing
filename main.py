# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 11:30:47 2016

@author: bubgum
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from function import *
from classfiturwarna import *
from classsobel import *
    
class main:

    sobel = classsobel()
    
    jumlah = 64
    
    fiturwarna = []
    
    #generate array index depend on color counter
    for arr in range(maksWarna):
        fiturwarna.append(0)
    
    warna = classfiturwarna()
    fiturWarna = combinedTexton
    
    
        

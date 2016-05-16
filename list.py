#import os
#import sys
import cv2
import numpy as np

im = cv2.imread("E:/py/images/1.bmp")
imheight, imwidth, imchannel = im.shape

b, g, r = cv2.split(im)

for x in range(imheight):
	for y in range(imwidth):
		b[x][y] = (64*r[x][y]/255)
		g[x][y] = (64*g[x][y]/255)
		r[x][y] = (64*b[x][y]/255)
#print b
#print g
#print r
	
hasil = cv2.merge((b,g,r))

cv2.imshow("RGB",hasil)
cv2.waitKey(100000000)
		




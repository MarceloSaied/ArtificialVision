# -*- coding: utf-8 -*-
"""
testeos de opencv
"""

import pandas as pd
print( "Pandas Version      "+pd.__version__)

import numpy as np
print ("NumPy Version       "+np.__version__)

#import matplotlib as mpl
#print "MathPlotLib Version "+mpl.__version__
from matplotlib import pyplot as plt

import cv2
print ("OpenCV Version      "+cv2.__version__)


# Load an color image in grayscale
img = cv2.imread('images1/IFTS12044.jpg',0)
img = cv2.imread("images1/whatsapp1.jpg",0)
#print (img)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img)

exit
cv2.imwrite('imggray.png',img)


k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
elif k == ord('m'): # wait for 's' key to save and exit
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
    cv2.destroyAllWindows()
    
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
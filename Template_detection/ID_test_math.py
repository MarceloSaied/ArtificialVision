import cv2
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



# 500 x 250
img1 = cv2.imread('McD_logo100.jpg')
img2 = cv2.imread('BigMac100.jpg')

add = img1 + img2
cv2.imshow('add1',add)

add = cv2.add(img1,img2)
cv2.imshow('add2',add)

weighted = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)
cv2.imshow('weighted',weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()
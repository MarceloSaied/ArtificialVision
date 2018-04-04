# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:31:18 2018

@author: MarceloS
"""

import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)
time.sleep(2)

while True:
    ret,frame = cam.read()
    cv2.imshow('webcam', frame)


cam.release()
cv2.destroyAllWindows() 
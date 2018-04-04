# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:35:31 2018

@author: MarceloS
"""

from matplotlib import pyplot as plt
import numpy as np

import cv2

face_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)


# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 200,
                       qualityLevel = 0.01,
                       minDistance = 10,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,3))

# Take first frame and find corners in it
ret, old_frame = cap.read()



cv2.imshow('Old_Frame', old_frame)
cv2.waitKey(0)
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
restart = True
#while restart == True:
face = face_classifier.detectMultiScale(old_gray, 1.2, 4)

if len(face) == 0:
    print ("This is empty")

for (x,y,w,h) in face:
    focused_face = old_frame[y: y+h, x: x+w]

cv2.imshow('Old_Frame', old_frame)

face_gray = cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)

gray = cv2.cvtColor(focused_face,cv2.COLOR_BGR2GRAY)

corners_t = cv2.goodFeaturesToTrack(gray, mask = None, **feature_params)
corners = np.int0(corners_t)

print (corners)

for i in corners:
    ix,iy = i.ravel()
    cv2.circle(focused_face,(ix,iy),3,255,-1)
    cv2.circle(old_frame,(x+ix,y+iy),3,255,-1)

plt.imshow(old_frame),plt.show()


# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while(1):
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, corners_t, None, **lk_params)

    # Select good points
    good_new = p1[st==1]
    good_old = corners_t[st==1]

    # draw the tracks
    print ("COLORING TIME!")
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        print (i)
        print( color[i])
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv2.circle(frame,(a, b),5,color[i].tolist(),-1)
        if i == 99:
            break
    img = cv2.add(frame,mask)

    cv2.imshow('frame',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()
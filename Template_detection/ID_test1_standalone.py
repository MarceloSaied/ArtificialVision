import cv2
#import pandas as pd
import numpy as np
#from matplotlib import pyplot as plt

import time



#-------------------------  variables  ----------------------------
#------------------------------------------------------------------
#templateImage = 'McDonalds_logoBW1-0.jpg'
#templateImage = 'McDonalds_logoBW1-grande.jpg'
templateImage = 'BigMac1.jpg'

img_orig = 'McDonaldsFlyer90.jpg'
#img_orig = 'McDonaldsFlyer_brillo.jpg'
#img_orig = 'McDonaldsFlyer_sepia.jpg'
#img_orig = 'McDonaldsFlyer_big.jpg' ------------??????????????
#img_orig = 'McDonaldsFlyer_100.jpg'

rotacion_orig = 330
threshold_orig = 0.98

#--------------functions -----------------
import FuncionesMias as f
#--------------main----------------
start_time = time.time()


def main():
    #-------- load imagenes --------
    template = cv2.imread(templateImage,0)
#    cv2.imshow('1_template',template) #------------------------------------------------
    w, h = template.shape[::-1]
    
    img_rgb_orig = cv2.imread(img_orig)
    img_gray1 = cv2.cvtColor(img_rgb_orig, cv2.COLOR_BGR2GRAY)
#    cv2.imshow('2_img_gray1',img_gray1)
    
    ######## --- loop rotacion y deteccion ---------------------------------------------
    encontardo = 0
    threshold = threshold_orig 
    while True:
        start_time_inter = time.time()
        rotacion = rotacion_orig
        while True:
            #----------------------------  rotation ------------------------------------
            img_gray_rotated = f.rotate_image4(img_gray1, rotacion)
            #cv2.imshow('img_gray_rotated',img_gray_rotated)
            img_rgb_orig_rotated = f.rotate_image4(img_rgb_orig, rotacion)
            #cv2.imshow('img_rgb_orig_rotated',img_rgb_orig_rotated)
            
            #-----------------------detecctar logo  ------------------------------------
            #---------------------------------------------------------------------------
            res = cv2.matchTemplate(img_gray_rotated,template,cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
#            print(loc)
            if  all(loc) :
                print("----------------",threshold," ",rotacion,"  ",loc)
                encontardo = 1
                break
                
            print(threshold," ",rotacion,"  ",loc)
            rotacion = rotacion + 1 
            if rotacion == 360: rotacion = 0
            if rotacion == rotacion_orig: break

        if encontardo == 1:break
        threshold = threshold - 0.02
        print(threshold)
        print("--- %s seconds ---" % (time.time() - start_time_inter))  
        if threshold <= 0.01:  break

    
    ######  ---- end loop rotation and detection
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_gray_rotated, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
#    cv2.imshow('DetectedGREY',img_gray_rotated)
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb_orig_rotated, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    cv2.imshow('DetectedRGB',img_rgb_orig_rotated)   #---------------------------------
    
    
    print("--- %s seconds ---" % (time.time() - start_time)) 
    cv2.imshow('1_template',template)    
    cv2.imshow('2_img_orig',img_rgb_orig)
    
main()
print("--- %s seconds ---" % (time.time() - start_time))  


    
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()

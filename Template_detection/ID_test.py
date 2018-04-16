#!/usr/bin/python

import sys
import cv2
import numpy as np
import time
import os
#from os import path

start_time = time.time()
#--------------functions -----------------
import FuncionesMias as f
#--------------main----------------

def main(templateImage,img_orig,rotacionStart_orig,rotacionEnd_orig,threshold_orig,orden,outFolder):
    orden = int(orden)
    rotacionStart_orig = int(rotacionStart_orig)
    if orden == -1:
        temp = rotacionStart_orig
        rotacionStart_orig = rotacionEnd_orig
        rotacionEnd_orig = temp
        del temp
    print(rotacionStart_orig , " -> " , rotacionEnd_orig)
    rotacionEnd_orig = int(rotacionEnd_orig)
     #-------- load imagenes --------
    template = cv2.imread(templateImage,0)                                #    cv2.imshow('1_template',template) 
    w, h = template.shape[::-1]
    
    img_rgb_orig = cv2.imread(img_orig)
    img_gray1 = cv2.cvtColor(img_rgb_orig, cv2.COLOR_BGR2GRAY)            #    cv2.imshow('2_img_gray1',img_gray1)
    ######## --- loop rotacion y deteccion ---------------------------------------------
    encontardo = -1
    threshold = float(threshold_orig)
    rotacionStart_orig =int(rotacionStart_orig)
    rotacion = rotacionStart_orig
    while True:
        if  os.path.exists("found.txt"): break
        print(rotacion)
        #----------------------------  rotation ------------------------------------
        rotacion = int(rotacion)
        img_gray_rotated = f.rotate_image4(img_gray1, rotacion)         #cv2.imshow('img_gray_rotated',img_gray_rotated)
        img_rgb_orig_rotated = f.rotate_image4(img_rgb_orig, rotacion)  #cv2.imshow('img_rgb_orig_rotated',img_rgb_orig_rotated)
        #-----------------------detecctar logo  ------------------------------------
        res = cv2.matchTemplate(img_gray_rotated,template,cv2.TM_CCOEFF_NORMED)
        loc = np.where( res >= threshold)
#        print(loc)
        if  all(loc) :
#            print("----------------",threshold," ",rotacion,"  ",loc)
            encontardo = 1
            nfile,ext = img_orig.split(".")
            entero, decimal = divmod(threshold, 1)
            cv2.imwrite(outFolder + nfile+"_up"+"_"+str(round(time.time()-start_time,2))+"_"+str(decimal)+".jpg", img_rgb_orig_rotated)  
            print(outFolder + nfile+"_up"+"_"+str(round(time.time()-start_time,2))+"_"+str(decimal)+".jpg")
            file = open("found.txt", "w")
#            file.write(nfile + "_up" + "_" + str(round(time.time() - start_time,2)) + "_" + str(decimal) + ".jpg") 
            file.write(str(decimal)) 
            file.close()
            break
            
        print(threshold," ",rotacion,"  ",loc)
        rotacion = rotacion + orden
        if rotacion == rotacionEnd_orig + orden :
            encontardo = 0
            break
        
#    for pt in zip(*loc[::-1]):
#        cv2.rectangle(img_gray_rotated, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
#    cv2.imshow('DetectedGREY',img_gray_rotated)
 
#    for pt in zip(*loc[::-1]):
#        cv2.rectangle(img_rgb_orig_rotated, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
#    cv2.imshow('DetectedRGB',img_rgb_orig_rotated)

        
#    cv2.imshow('1_template',template)    
#    cv2.imshow('2_img_orig',img_rgb_orig)
        
    return encontardo
   
#testeo ####################################################
#templateImage = 'BigMac1.jpg'
#img_orig = 'McDonaldsFlyer_100.jpg'
#rotacionStart = 170
#rotacionEnd = 180        
#threshold  = 0.94
#res = main(templateImage,img_orig,rotacionStart,rotacionEnd,threshold)
#print("--- %s seconds ---" % (time.time() - start_time),res)  
##############################################################

    
if len(sys.argv) == 8: 
    templateImage = sys.argv[1]
    img_orig = sys.argv[2]
    rotacionStart = sys.argv[3]
    rotacionEnd = sys.argv[4]       
    threshold  = sys.argv[5]    
    order  = sys.argv[6]  
    outFolder = sys.argv[7]  
    res = main(templateImage,img_orig,rotacionStart,rotacionEnd,threshold,order,outFolder)
#    print("--- %s seconds ---" % (time.time() - start_time),res)  
    print(res)  
else:
    print("--- %s seconds ---" % (time.time() - start_time),-1)  
#    print(res) 

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()





# -*- coding: utf-8 -*-
"""
main_logo.py
inicia la deteccion distribuida , . una instancia por cada 90 grados
Created on Fri Mar 23 14:13:34 2018

@author: MarceloS
"""
import sys
import os
import subprocess as sp
import time

DETACHED_PROCESS = 0x00000008

outFolder = "/home/bp/logo/out/"    
#---------------------------------------
def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        print("")
#        raise ValueError("file {} is not a file or dir.".format(path))

def midTreashold():
    if os.path.isfile("mid.txt"):
        file = open("mid.txt", "r")
        ret = file.readline()
        file.close()
    else:
        ret=0.94
    return ret

#---------------------- help --------------------------------------
print("")
print("--------------------------------------------------")
print("Usage: python3 <img_orig str jpg> [mappers int = 4] ")
#-------------------------  variables  ----------------------------
#------------------------------------------------------------------
mappers = 4
#templateImage = 'McDonalds_logoBW1-0.jpg'
#templateImage = 'McDonalds_logoBW1-grande.jpg'
templateImage = 'BigMac1.jpg'
#templateImage = 'templateAcindar1.jpg'

#img_orig = 'McDonaldsFlyer_brillo.jpg'
#img_orig = 'McDonaldsFlyer_sepia.jpg'
#img_orig = 'McDonaldsFlyer_big.jpg' ------------??????????????
#img_orig = 'McDonaldsFlyer90.jpg'
img_orig = 'McDonaldsFlyer_100.jpg'
#img_orig = 'boletaAcindar1.jpg'

#------------------------
if len(sys.argv) == 3:
    mappers = int(sys.argv[2])
    img_orig  = sys.argv[1]
if len(sys.argv) == 2:
        mappers = int(sys.argv[1])
  
        
print("using: ",mappers," mappers")
print("procesing file : ",img_orig)
#----------------------------------------------------
threshold_mid = float(midTreashold())
threshold_min = round(threshold_mid-0.05,2)
threshold_max = round(threshold_mid+0.05,2)
print("Treshold",threshold_mid)
print("--------------------------------------------------")
print("")
pArr = []
entero, decimal = divmod(int(360/mappers), 1)
rangoBase = entero
print(rangoBase)

print(decimal)
anguloInit = 0
rotacionStart = anguloInit
counter = 0
orden = -1
threshold = threshold_max 
flagFileName="found.txt"
remove(flagFileName)    
while threshold >= threshold_min:
    rotacionStart = anguloInit
    for m  in range(0, mappers):
        orden=orden*-1
        rotacionEnd = rotacionStart + (rangoBase - 1)
        print("Angulos set ",m, "/",mappers , "  cant=",rangoBase," = ",rotacionStart," ",rotacionEnd,"  " ,threshold,str(orden))
        comm = 'python ' + "ID_test.py" + " " + templateImage + " " + img_orig + " " + str(rotacionStart) + " " + str(rotacionEnd) + " " +str(threshold) +" "+str(orden) +" "+str(outFolder)
        print(comm )
    #    child = sp.Popen(comm, stdout=sp.PIPE, shell=True)  -------------------
        if  os.path.exists("found.txt"): break
        child = sp.Popen(comm, shell=True,stdout=sp.PIPE)
        counter += 1
    #    child = sp.Popen(comm, creationflags=DETACHED_PROCESS,shell=True)  -------------------
    #    print("-->  ",child)   -------------------
    #    streamdata = child.communicate()  -------------------
    #    print(streamdata)   -------------------
    #    rc = child.returncode   ------------------- 
    #    print("RC = " + str(rc)) -------------------
        
    #    streamdata,err = child.communicate()[0]  --------------
    #    streamdata = child.communicate()[0] ------------
    #    print(err)  -------------------
    
        rotacionStart = rotacionEnd +1
        
    threshold = round(threshold - 0.02,2)
    time.sleep(5)

#    pArr.append(res)
#    print(pArr[0].communicate())
#    print(pArr[0].communicate()[1])
#    print(pArr)



#        threshold = threshold - 0.02
#        print(threshold)
#        print("--- %s seconds ---" % (time.time() - start_time_inter))  
#        if threshold <= 0.01:  break

print("treads = " ,counter)





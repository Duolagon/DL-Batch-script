#coding:utf-8
# 统计类别像素比例
import cv2
import numpy as np
import glob
import os
from shutil import copy
def mkfile(file):
    if not os.path.exists(file):
        os.makedirs(file)
mkfile('S')
mkfile('B')
mkfile('M')

pngpath = glob.glob('*.png')
zmat = 0
count = 0
for path in pngpath:
    count+=1
    if "prediction" in path:
        mask = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        a1 = mask == 0
        a1_count = len(mask[a1])
        print(count)
        zmat=a1_count/(mask.shape[0]*mask.shape[1])
        zmat = 1-zmat
        if 0<zmat<0.2 or zmat ==0:
            picscale = "S"
            image_path = picscale+'/'
            copy(path, image_path)
            origine =(path[1:]).replace("prediction.png","image.png")
            copy(origine, image_path)
        elif 0.2<zmat<1/3 or zmat==0.2:
            picscale = "M"
            image_path = picscale+'/'
            copy(path, image_path)
            origine =(path[1:]).replace("prediction.png","image.png")
            copy(origine, image_path)
        elif 1/3<zmat<1 or zmat==1/3:
            picscale = "B"
            image_path = picscale+'/'
            copy(path, image_path)
            origine =(path[1:]).replace("prediction.png","image.png")
            copy(origine, image_path)
        else:
            picscale = "Other"
        new_name = picscale+path
        #os.rename(path, new_name)

        print(pngpath)
    print(zmat)
picscale = "SBM"
for i in picscale:
    pngpathnew = glob.glob(i+'/''*.png')
    for path in pngpathnew:
            if path[2] =="S" :
                new_name = path.replace("S0","0")
                os.rename(path, new_name)
            elif path[2] =="M" :
                new_name = path.replace("M0","0")
                os.rename(path, new_name)
            elif path[2] =="B" :
                new_name = path.replace("B0","0")
                os.rename(path, new_name)

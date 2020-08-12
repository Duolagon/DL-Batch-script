#coding:utf-8
# 统计类别像素比例
import cv2
import numpy as np
import glob

pngpath = glob.glob('SegmentationClassRaw/*.png')
zmat = np.zeros([4], dtype = np.float32)
count = 0
for path in pngpath:
    count+=1
    mask = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    for pixelvalue in range(4):
        a1 = mask == pixelvalue
        a1_count = len(mask[a1])
        zmat[pixelvalue]+=a1_count/(mask.shape[0]*mask.shape[1])
zmat= zmat/ count
print(zmat)
list  = []
for a in zmat:
    b = zmat[0]/a
    list.append(b)
    print(list)


# coding：<encoding name> ： # coding: utf-8
import cv2
import glob as gb
import numpy as np
from skimage import draw
import matplotlib.pyplot as plt
from skimage.measure import regionprops
import time



def bodymid(imagepath):
    imge = cv2.imread(imagepath)
    gray = cv2.cvtColor(imge, cv2.COLOR_BGR2GRAY)
    # 大津法二值化
    dst= np.where(gray ==160,160,0)
    property = regionprops(dst)
    center = property[0].centroid
    return (center[0], center[1], gray)


if __name__ == "__main__":
    img_path = gb.glob("test51.jpg")
    for path in img_path:

        #path = 'test25.png'
        t0 = time.time()
        c,d,gray_= bodymid(path)
        t1 = time.time()
        print('totol', (t1 - t0) * 1000)

        rr, cc = draw.circle(c, d, 10)
        draw.set_color(gray_, [rr, cc], [255])
        plt.imshow(gray_)
        plt.show()
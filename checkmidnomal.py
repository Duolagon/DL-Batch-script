# coding：<encoding name> ： # coding: utf-8
import cv2
import glob as gb
import numpy as np
from skimage import draw
import matplotlib.pyplot as plt
from skimage.measure import label
import time



def largestConnectComponent(bw_img):
    labeled_img, num = label(bw_img, connectivity=1, background=0, return_num=True)
    # plt.figure(), plt.imshow(labeled_img, 'gray')
    max_label = 0
    max_num = 0
    for i in range(1, num + 1):  # 这里从1开始，防止将背景设置为最大连通域
        if np.sum(labeled_img == i) > max_num:
            max_num = np.sum(labeled_img == i)
            max_label = i
        lcc = (labeled_img == max_label)

    return lcc

def bodymid(imagepath):
    t0 = time.time()

    imge = cv2.imread(imagepath)
    gray = cv2.cvtColor(imge, cv2.COLOR_BGR2GRAY)
    a = np.unique(gray)
    gray_ = gray.copy()
    m, n = len(gray[0]) - 1, len(gray) - 1
    t1 = time.time()
    print('begin',(t1 - t0) * 1000)
    if len(a)<3:
        print(imagepath)
    else:
    # 大津法二值化
        dst= np.where(gray ==160,160,0)
        #retval, dst = cv2.threshold(gray, 80, 255, 0)
        t2 = time.time()
        print('dst', (t2 - t1) * 1000)

        lcc = largestConnectComponent(dst)
        t3= time.time()
        print('lcc', (t3 - t2) * 1000)

        gray[lcc == False] = 0

        if 240 in a:
            dst2 = np.where(gray_ == 240, 240, 0)
            #retval2, dst2 = cv2.threshold(gray_, 160, 255, 0)
            lcc2 = largestConnectComponent(dst2)
            gray[lcc2 == True] = 240
        t4= time.time()
        print('lcc2', (t4 - t3) * 1000)

        res = []
        M = []
        O = []
        for i in [160,240]:
            l, r, t, b = 0,m,0,n
            if i ==160:                                       #主体+负载
                while l<r:
                    if i not in gray[:,l]:
                        l+=1
                    elif i not in gray[:,r]:
                        r-=1
                    else:
                        break
            while t<b:
                if i not in gray[t,:]:
                    t+=1
                elif i not in gray[b,:]:
                    b-=1
                else:
                        break
            if i == 160:#主体
                M.append(l)
                M.append(r)
                M.append(t)
                M.append(b)
            if len(a)>3:
                if i == 240:#负载
                    O.append(t)
        if 240 not in a:
            res.append(((M[0] + M[1]) // 2, (M[2] + M[3]) // 2))
        else:
            res.append(((M[0]+M[1])//2,(M[2]+O[0])//2))#主体
        t5= time.time()
        print('end', (t5 - t4) * 1000)
        print('total', path,(t5 - t0) * 1000,[m+1,n+1])
        for z in res:  #
            c ,d =int(round(z[0])) ,int (round(z[1]))
            return(c,d,gray_)

if __name__ == "__main__":
    img_path = gb.glob("test51.jpg")
    for path in img_path:

        #path = 'test25.png'
        c,d,gray_= bodymid(path)


        rr, cc = draw.circle(d, c, 10)
        draw.set_color(gray_, [rr, cc], [255])
        plt.imshow(gray_)
        plt.show()
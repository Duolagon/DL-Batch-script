#from yolo import YOLO
from PIL import Image
import numpy as np
import cv2
import time
import os
#yolo = YOLO()
name ="1024-13"
videopath = "./s/"+name+".mp4"
capture=cv2.VideoCapture(videopath)

desktop_path = "./b/"  # 新创建的txt文件的存放路径

full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档



# fps = 0.0
# count= 0
# while(capture):
#     t1 = time.time()
#     # 读取某一帧
#     count+=1
#     print(count)
#     ref,frame=capture.read()
#     # 格式转变，BGRtoRGB
#     frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#     # 转变成Image
#     frame = Image.fromarray(np.uint8(frame))
#
#     # 进行检测
#     frame = np.array(frame)
#
#     # RGBtoBGR满足opencv显示格式
#     frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
#
#     fps  = ( fps + (1./(time.time()-t1)) ) / 2
#     print("fps= %.2f"%(fps))
#     #frame = cv2.putText(frame, "fps= %.2f"%(fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     if count%50==0:
#     #cv2.imshow("video",frame)
#         cv2.imwrite("./b/test"+str(count)+name+'.png', frame.astype(np.uint8))
imagenamelist = os.listdir(desktop_path)
for image in imagenamelist:
    if 'png'in image  :
        image = image.replace('.png','')
        file = open(full_path, 'a')
        file.write('\n'+image)
        file.close()


    # c= cv2.waitKey(30) & 0xff
    # if c==27:
    #     capture.release()
    #     break

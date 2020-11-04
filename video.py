# -*- coding: UTF-8 -*-
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time


# # 图片合成视频
# def picvideo(path, size):
#     # path = r'C:\Users\Administrator\Desktop\1\huaixiao\\'#文件路径
#     filelist = os.listdir(path)  # 获取该目录下的所有文件名
#
#     '''
#     fps:
#     帧率：1秒钟有n张图片写进去[控制一张图片停留5秒钟，那就是帧率为1，重复播放这张图片5次]
#     如果文件夹下有50张 534*300的图片，这里设置1秒钟播放5张，那么这个视频的时长就是10秒
#     '''
#     fps = 12
#     # size = (591,705) #图片的分辨率片
#     file_path = r"C:\Users\Administrator\Desktop\aa1" + str(int(time.time())) + ".mp4"  # 导出路径
#     fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')  # 不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）
#
#     video = cv2.VideoWriter(file_path, fourcc, fps, size)
#
#     for item in filelist:
#         if item.endswith('.png'):  # 判断图片后缀是否是.png
#             item = path + '/' + item
#             img = cv2.imread(item)  # 使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
#             video.write(img)  # 把图片写进视频
#
#     video.release()  # 释放
#
#
# picvideo(r'C:\Users\Administrator\Desktop\1\huaixiao\\', (591, 705))

def remiximg(image, mask):
    im_color = cv2.applyColorMap(mask, 2)
    cv_imgmask = cv2.cvtColor(im_color, cv2.COLOR_BGR2BGRA)
    cv_imgmask[:, :, 3] = 128  # 整体透明度设为一半
    cv_imgmask[:, :, 3][np.where(cv_imgmask[:, :, 0] == 128)] = 0  # 背景透明度设为0
    cv_imgmask[:, :, 1][np.where(cv_imgmask[:, :, 1] == 192)] = 0  # 让蓝色更蓝
    # cv_imgmask[:, :, 2][np.where(cv_imgmask[:, :, 2] == 255)] = 0 # 黄色变成绿色
    imgsrc = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2BGRA))
    pil_imgmask = Image.fromarray(cv_imgmask).convert('RGBA')
    res = np.asarray(Image.alpha_composite(imgsrc, pil_imgmask))
    return res

file = 'True'
image_class = [cla for cla in os.listdir(file) if ".txt" not in cla]
count = 0
for i in image_class:
    if (file + '/' + 'combine' + i) not in image_class:
        if '_image' in i and 'combine' not in i:
            imagepath = file + '/' + i
            image = cv2.imread(imagepath)
            other = i.replace('image', 'prediction')
            imagepath2 = file + '/' + other
            image2 = cv2.imread(imagepath2)

            # grid_spec = gridspec.GridSpec(1, 4, width_ratios=[6, 6, 6, 1])
            #
            # plt.subplot(grid_spec[0])
            # plt.imshow(image)
            #plt.axis('off')
            # plt.title('input image')
            #
            # plt.subplot(grid_spec[1])
            # seg_image = label_to_color_image(seg_map).astype(np.uint8)
            #plt.imshow(image2)
            #plt.axis('off')
            # plt.title('segmentation map')
            #
            # plt.subplot(grid_spec[2])
            #plt.imshow(image)
            temp = remiximg(image,image2)
            #plt.imshow(image2, alpha=0.7)
            #plt.axis('off')
            # plt.title('segmentation overlay')

            # unique_labels = np.unique(seg_map)
            # ax = plt.subplot(grid_spec[3])
            # plt.imshow(
            # FULL_COLOR_MAP[unique_labels].astype(np.uint8), interpolation='nearest')
            # ax.yaxis.tick_right()
            # plt.yticks(range(len(unique_labels)), LABEL_NAMES[unique_labels])
            # plt.xticks([], [])
            # ax.tick_params(width=0.0)
            #height, width, channels = image.shape
            # 如果dpi=300，那么图像大小=height*width
            #plt.figure(figsize=(9.6, 5.76))
            #fig.set_size_inches(width / 100.0 / 3.0, height / 100.0 / 3.0)
            # plt.gca().xaxis.set_major_locator(plt.NullLocator())
            # plt.gca().yaxis.set_major_locator(plt.NullLocator())
            # plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
            # plt.margins(0, 0)
            cv2.imwrite(file + '/' + i.replace('.png', 'combine.png') , temp)
            # plt.savefig(file + '/' + 'combine' + i,bbox_inches="tight", pad_inches=0.0,dpi = 100)
            # #plt.grid('off')
            #
            # plt.cla()
            # plt.close("all")
            count += 1
            print(count)


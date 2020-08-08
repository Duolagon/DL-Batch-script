import os
from shutil import copy
import random
import numpy as np
import cv2
from PIL import ImageFile
from PIL import Image
ImageFile.LOAD_TRUNCATED_IMAGES = True
import numpy as np
#from keras.applications.imagenet_utils import decode_predictions
#from keras.preprocessing import image
#from keras.applications import *
import glob
#from model import MobileNetV2
#import tensorflow as tf
import os
import json
import time
#tf.enable_eager_execution()



def mkfile(file):
    if not os.path.exists(file):
        os.makedirs(file)


file = ("jingling4")

image_class = [cla for cla in os.listdir(file) if ".txt" not in cla]


widthmost = 0
heightmost = 0
for i in image_class:
    if '.jpg' in i :
        filepath = 'C:\\Users\\hursk\\Documents\\Tencent Files\\1192018338\\FileRecv'+'\\'+file +'\\'+ i# 把图片读取出来放到列表中
        image = cv2.imread(filepath)
        width = image.shape[0]
        height= image.shape[1]
        if width > widthmost:
           widthmost=width
        if height > heightmost:
           heightmost = height
print(widthmost,heightmost)

for i in image_class:
    if '.jpg' in i :
        filepath = 'C:\\Users\\hursk\\Documents\\Tencent Files\\1192018338\\FileRecv'+'\\'+file +'\\'+ i# 把图片读取出来放到列表中
        image = cv2.imread(filepath)
        width = image.shape[0]
        height= image.shape[1]
        if width == 2680 and height == 4020:
            print(i)


import os
from shutil import copy
import random
import numpy as np


def mkfile(file):
    if not os.path.exists(file):
        os.makedirs(file)


file = 'abc'
image_class = [cla for cla in os.listdir(file) if ".txt" not in cla]
mkfile('01')

mkfile('02')




split_rate = 0.5
num = len(image_class)
train_index =[]
z = k= int(num * split_rate)
count = 0
for i in range(0,z):
    train_index.append(i)
for cla in image_class:
    if count in train_index:
        image_path = file +'/'+cla
        new_path = '01'
        copy(image_path, new_path)
    else:
        image_path = file +'/'+cla
        new_path = '02'
        copy(image_path, new_path)
    count += 1



print("processing done!")

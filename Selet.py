
from PIL import ImageFile
from PIL import Image
ImageFile.LOAD_TRUNCATED_IMAGES = True

import os




def mkfile(file):
    if not os.path.exists(file):
        os.makedirs(file)


file = ("精灵4的视频4_000")

image_class = [cla for cla in os.listdir(file) if ".txt" not in cla]

for i in image_class:
    path = file + '/' + i
    j = i
    k= j.replace('精灵4的视频4_','')
    z =  k.replace('.jpg','')
    z = int(z)
    if z %5 != 0:
        os.remove(path)


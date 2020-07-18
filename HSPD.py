import os
from hashlib import md5

def file_name(file_path):

    for root, dirs, files in os.walk(file_path):

        return dirs




path = 'C:/Users/hursk/Documents/Tencent Files/1192018338/FileRecv/Image-Downloader-master/download_images/'
f = open(path + 'md5.txt', 'w')
list = []

list1 = []
for clc in file_name(path):
    print(clc)
    path_clc = path + clc


#得到所有图片的路径，加到列表list1中
    root, _, files = next(os.walk(path_clc))
    for i in range(len(files)):
        line = path_clc + '/' + str(files[i])
        list1.append(line)

#计算每张图片的md5值，并将图片路径与其md5值整合到列表list中
for n in range(len(list1)):
    hash = md5()
    img = open(list1[n], 'rb')
    hash.update(img.read())
    img.close()
    list2 = [list1[n], hash.hexdigest()]
    f.write(str(list2)+'\n')
    list.append(list2)

#两两比较md5值，若相同，则删去一张图片
m = 0
while m < len(list):
    t = m + 1
    while t < len(list):
        if list[m][1] == list[t][1]:
            os.remove(list[t][0])
            print(list[t][0])
            del list[t]
        else:
            t += 1
    m += 1




import cv2
import matplotlib.pyplot as plt
import os
from matplotlib import gridspec


file = '0000'
image_class = [cla for cla in os.listdir(file) if ".txt" not in cla]
for i in image_class:
    if '.jpg' in i and 'combin' not in i:
        imagepath = './'+file +'/'+ i
        image = cv2.imread(imagepath)
        imagepath2 = './'+file + '/'+'2007_000033.png'
        image2 = cv2.imread(imagepath2)
        plt.figure(figsize=(15, 5))
        grid_spec = gridspec.GridSpec(1, 4, width_ratios=[6, 6, 6, 1])

        plt.subplot(grid_spec[0])
        plt.imshow(image)
        plt.axis('off')
        plt.title('input image')

        plt.subplot(grid_spec[1])
        #seg_image = label_to_color_image(seg_map).astype(np.uint8)
        plt.imshow(image2)
        plt.axis('off')
        plt.title('segmentation map')

        plt.subplot(grid_spec[2])
        plt.imshow(image)
        plt.imshow(image2, alpha=0.7)
        plt.axis('off')
        plt.title('segmentation overlay')

        #unique_labels = np.unique(seg_map)
        #ax = plt.subplot(grid_spec[3])
        #plt.imshow(
            #FULL_COLOR_MAP[unique_labels].astype(np.uint8), interpolation='nearest')
        #ax.yaxis.tick_right()
        #plt.yticks(range(len(unique_labels)), LABEL_NAMES[unique_labels])
        #plt.xticks([], [])
        #ax.tick_params(width=0.0)
        plt.savefig('./' + file + '/' + 'combin' + i)
        plt.grid('off')



# BGR to RGB



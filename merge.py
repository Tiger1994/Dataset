import matplotlib.pyplot as plt
import cv2
import math
import os
import numpy as np


def main():
    file_path = 'C:\\Users\\Tiger\\OneDrive - stu.scu.edu.cn\\Papers\\Mine\\Graduate\\figures\\chapter2\\Image_sets'
    set = 'Historical'
    image_path = file_path+'\\'+set
    cols_num = 5
    pixels = 200
    space = 2
    width_pixels = 1080
    images = []
    for name in os.listdir(image_path):
        image = plt.imread(image_path+'\\'+name, )
        images.append(image)

    rows_num = math.ceil(float(len(images))/cols_num)
    merge = np.ones([rows_num*(pixels+space), cols_num*(pixels+space), 3])*255

    for i, image in enumerate(images):
        row = int(i / cols_num)
        col = i % cols_num
        image = cv2.resize(image, (pixels, pixels))
        if len(image.shape) == 2:
            image = np.expand_dims(image, axis=2)
        row_start = row*(pixels+space)
        col_start = col*(pixels+space)
        merge[row_start:row_start+pixels, col_start:col_start+pixels, :] = image

    highth_pixel = int(merge.shape[0]/(merge.shape[1]/width_pixels))
    merge = cv2.resize(merge, (width_pixels, highth_pixel))
    plt.axis('off')
    plt.imshow(merge, cmap=plt.cm.jet)
    plt.show()
    merge = merge[:, :, ::-1]
    cv2.imwrite(file_path+'\\'+set+'.png', merge*255)


if __name__ == '__main__':
    main()

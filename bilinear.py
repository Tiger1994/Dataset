import os
import matplotlib.pyplot as plt
import numpy as np
import cv2


def main():
    set_path = r'C:\Users\Tiger\OneDrive - stu.scu.edu.cn\Papers\Mine\Graduate\figure\chapter2\Image_sets'
    set = ['Set5', 'Set14', 'B100', 'Urban100', 'Manga109']
    rpath = r'C:\Users\Tiger\OneDrive - stu.scu.edu.cn\Papers\Mine\Graduate\figure\chapter3\perceptual\result\Bilinear'

    for set_name in set:
        image_path = set_path+'\\'+set_name
        save_path = rpath+'\\'+set_name
        if not os.path.isdir(save_path):
            os.makedirs(save_path)
        for name in os.listdir(image_path):
            image_name = image_path+'\\'+name
            image = plt.imread(image_name)
            if len(image.shape) == 2:
                image = np.expand_dims(image, axis=2)
                image = np.concatenate((image, image, image), axis=2)

            shape = image.shape
            down_shape = (shape[1]//4, shape[0]//4)
            image = cv2.resize(image, down_shape)
            image = cv2.resize(image, (shape[1], shape[0]))

            save_name = save_path+'\\'+name
            plt.imsave(save_name, image)
            print("Complete: ", name)
            # plt.imshow(image)
            # plt.show()

    a = 0


if __name__ == '__main__':
    main()

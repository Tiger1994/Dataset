import os
import numpy as np
import matplotlib.pyplot as plt
import cv2


def main():
    file_path = 'C:\\Users\\Tiger\\OneDrive - stu.scu.edu.cn\\Papers\\Mine\\Graduate\\figures\\chapter2\\Loss_compare'
    images = []

    rows_start = 100
    cols_start = 40
    rows_space = 60
    cols_space = 150
    for name in os.listdir(file_path):
        image = plt.imread(file_path+'\\'+name)
        images.append(image)

        shape = image.shape
        patch = image[rows_start:rows_start+rows_space, cols_start:cols_start+cols_space, :]
        cols_m = shape[1]
        rows_m = int(rows_space*(shape[1]/cols_space))
        patch_m = cv2.resize(patch, (cols_m, rows_m))

        patch_m = patch_m[:, :, ::-1]
        save_path = file_path+'\\'+'path'+name
        cv2.imwrite(save_path, patch_m)


if __name__ == '__main__':
    main()

import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    file_path = 'C:\\Users\\Tiger\\OneDrive - stu.scu.edu.cn\\Papers\\Mine\\Graduate\\figures\\chapter2\\Image_sets'
    set = 'BSDS100'
    image_path = file_path+'\\'+set
    width_count = 0
    highth_count = 0
    num = 0
    for name in os.listdir(image_path):
        image = plt.imread(image_path+'\\'+name)
        width_count += image.shape[0]
        highth_count += image.shape[1]
        num += 1

    print('Average width: ', width_count/num)
    print('Average highth: ', highth_count/num)


if __name__ == '__main__':
    main()

import json
import cv2
import matplotlib.pyplot as plt
import os
import numpy as np
import math
from PIL import ImageFont, ImageDraw, Image, ImageFile


def one_iter(name, opt, setting_path):
    print("Image: ", name)
    image_name = name
    saving_path = setting_path
    saving_path = saving_path+'\\'+image_name
    if not os.path.exists(saving_path):
        os.makedirs(saving_path)

    name = opt[image_name]['dataset']+'\\'+opt[image_name]['name']
    top_left = opt[image_name]['top_left']
    bottom_right = opt[image_name]['bottom_right']

    col = 5
    row = math.ceil(float(len(opt['methods']))/col)

    idx = 0
    width = bottom_right[1]-top_left[1]
    highth = bottom_right[0]-top_left[0]
    wspace = 12
    hspace = 3
    merge = np.ones([(width+wspace)*row-wspace//5, (highth+hspace)*col-hspace, 3]) * 255

    plt.rc('font', family='Times New Roman')
    plt.figure()
    for method in opt['methods']:
        print("Processing: ", method)
        image_path = opt['methods'][method]+'\\'+name
        image = Image.open(image_path).convert('RGB')
        image = np.asanyarray(image)
        if method == 'MemNet':
            patch = image[top_left[1]-4:bottom_right[1]-4, top_left[0]-4:bottom_right[0]-4, :]
        else:
            patch = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0], :]
        patch_name = '0_'+method+'.png'
        saving_patch = saving_path+'\\'+patch_name
        plt.imsave(saving_patch, patch)

        row_idx = idx // col
        col_idx = idx % col
        idx += 1
        row_start = row_idx*(width+wspace)
        col_start = col_idx*(highth+hspace)
        merge[row_start:row_start+width, col_start:col_start+highth, :] = patch

        line_size = int((image.shape[0]+image.shape[1])//1000+1)
        image = cv2.rectangle(image, (top_left[0], top_left[1]), (bottom_right[0], bottom_right[1]), (255, 0, 0),
                              line_size)
        if method == 'GT':
            red_image = image
        saving_name = method+'.png'
        saving_name = saving_path+'\\'+saving_name
        plt.imsave(saving_name, image)

    final_col = 1080
    shape = merge.shape
    up_rate = final_col/shape[1]
    final_row = int(shape[0]*up_rate)
    merge = cv2.resize(merge, (final_col, final_row))
    width = int(width*up_rate)
    highth = int(highth*up_rate)
    wspace = int(wspace*up_rate)
    hspace = int(hspace*up_rate)

    merge = merge.astype('uint8')
    merge = Image.fromarray(merge)
    draw = ImageDraw.Draw(merge)
    font_size = 30
    font = ImageFont.truetype(r"C:\Windows\Fronts\times.ttf", font_size, encoding="unic")
    idx = 0
    for method in opt['methods']:
        row_idx = idx // col
        col_idx = idx % col
        idx += 1
        row_start = row_idx*(width+wspace)
        col_start = col_idx*(highth+hspace)
        r = int(row_start+width+font_size/10)
        c = int(col_start+highth/2-len(method)*font_size/4)
        draw.text((c, r), method, font=font, fill='black')
    merge = np.array(merge)
    # plt.imshow(merge)
    # plt.axis('off')
    # plt.show()
    merge_name = 'merge.png'
    merge_name = saving_path+'\\'+merge_name
    plt.imsave(merge_name, merge)

    merge_shape = merge.shape
    red_shape = red_image.shape
    ratio = red_shape[0]/merge_shape[0]
    row_num = merge_shape[0]
    col_num = int(red_shape[1]/ratio)
    red_image = cv2.resize(red_image, (col_num, row_num))
    white_line = np.ones([row_num, hspace, 3])*255
    white_line = white_line.astype('uint8')
    final_image = np.concatenate([red_image, white_line, merge], axis=1)

    # shape = final_image.shape
    # up_rate = final_col/shape[1]
    # final_row = int(shape[0]*up_rate)
    # final_image = cv2.resize(final_image, (final_col, final_row))
    # plt.imshow(final_image)
    # plt.axis('off')
    # plt.show()
    final_name = setting_path+'\\'+opt[image_name]['name']
    plt.imsave(final_name, final_image)


def main():
    setting_path = 'C:\\Users\\Tiger\\OneDrive - stu.scu.edu.cn\\Papers\\Mine\\Graduate\\figure\\chapter4\\perceptual'
    setting_file = setting_path + '\\opt_new.json'
    with open(setting_file, 'r') as f:
        opt = json.load(f)

    for name in opt:
        if not (name == 'methods'):
            one_iter(name, opt, setting_path)
        # if name == 'KarappoHighschool':
        #     one_iter(name, opt, setting_path)


if __name__ == '__main__':
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    main()

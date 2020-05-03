import matplotlib.pyplot as plt
import cv2
import json
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def one_iter(json_path, image_name, opt):
    print('Image: ', image_name)
    # save_path = json_path+'\\'+image_name
    # if not os.path.isdir(save_path):
    #     os.mkdir(save_path)

    rspace = 5
    cspace = 8

    set_name = opt[image_name]['dataset']
    GT_path = opt['methods']['GT']+'\\'+set_name+'\\'+opt[image_name]['name']
    GT = plt.imread(GT_path)

    shape = GT.shape

    col_ratio = 0.33
    col_row_ration = 5/1.5
    top_left = opt[image_name]['top_left']
    col_num = int(shape[1]*col_ratio)
    row_num = int(col_num/col_row_ration)

    bottom_right = [top_left[0]+col_num, top_left[1]+row_num]
    row = bottom_right[1]-top_left[1]
    col = bottom_right[0]-top_left[0]

    final_row = int(row/(col/shape[1]))
    final_col = shape[1]

    font_size = int(shape[1]/12)
    wordspace = int(font_size*1.2)

    method_num = len(opt['methods'])
    merge = np.ones([shape[0]+rspace+final_row+wordspace, (shape[1]+cspace)*method_num-cspace, 3])*255
    merge = merge.astype('uint8')

    idx = 0
    for method in opt['methods']:
        print('Processing: ', method)
        image = Image.open(opt['methods'][method]+'\\'+set_name+'\\'+opt[image_name]['name'])
        image = np.asanyarray(image.convert('RGB'))
        if not (image.shape[0] == shape[0]):
            image = cv2.resize(image, (shape[1], shape[0]))
        patch = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0], :]
        patch = cv2.resize(patch, (final_col, final_row))

        line_size = int((image.shape[0]+image.shape[1])//800+1)
        image = cv2.rectangle(image, (top_left[0], top_left[1]), (bottom_right[0], bottom_right[1]), (0, 0, 255),
                              line_size)

        image_row = 0
        image_col = idx*(shape[1]+cspace)
        merge[image_row:image_row+shape[0], image_col:image_col+shape[1], :] = image
        patch_row = shape[0]+rspace
        patch_col = image_col
        merge[patch_row:patch_row+final_row, patch_col:patch_col+final_col, :] = patch
        idx = idx+1

    merge = Image.fromarray(merge)
    draw = ImageDraw.Draw(merge)
    font = ImageFont.truetype(r"C:\Windows\Fronts\times.ttf", font_size, encoding="unic")
    idx = 0
    for method in opt['methods']:
        text_row = shape[0]+1.5*rspace+final_row
        text_col = idx*(shape[1]+cspace)+int(shape[1]/2)-int(len(method)*font_size/5)
        draw.text((text_col, text_row), method, font=font, fill='black')
        idx = idx+1
    merge = np.array(merge)

    # plt.imshow(merge)
    # plt.axis('off')
    # plt.show()

    save_col = 3600
    m_shape = merge.shape
    save_row = int(m_shape[0]/(m_shape[1]/save_col))
    merge = cv2.resize(merge, (save_col, save_row))
    save_path = json_path+'\\'+image_name+'.png'
    plt.imsave(save_path, merge)


def main():
    json_path = r'C:\Users\Tiger\OneDrive - stu.scu.edu.cn\Papers\Mine\Graduate\figure\chapter5\perceptual_gan'
    json_name = 'opt.json'
    json_file = json_path+'\\'+json_name
    with open(json_file) as f:
        opt = json.load(f)

    for image_name in opt:
        if not image_name == 'methods':
            one_iter(json_path, image_name, opt)
    a =  0


if __name__ == '__main__':
    main()

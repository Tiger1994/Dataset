import matplotlib.pyplot as plt
from PIL import Image
import os
import math
import numpy as np
import cv2


def SSIM(img1, img2, shave_border=0):
    height, width = img1.shape[:2]
    img1 = img1[shave_border:height - shave_border, shave_border:width - shave_border]
    img2 = img2[shave_border:height - shave_border, shave_border:width - shave_border]

    C1 = (0.01 * 255)**2
    C2 = (0.03 * 255)**2

    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    kernel = cv2.getGaussianKernel(11, 1.5)
    window = np.outer(kernel, kernel.transpose())

    mu1 = cv2.filter2D(img1, -1, window)[5:-5, 5:-5]  # valid
    mu2 = cv2.filter2D(img2, -1, window)[5:-5, 5:-5]
    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.filter2D(img1**2, -1, window)[5:-5, 5:-5] - mu1_sq
    sigma2_sq = cv2.filter2D(img2**2, -1, window)[5:-5, 5:-5] - mu2_sq
    sigma12 = cv2.filter2D(img1 * img2, -1, window)[5:-5, 5:-5] - mu1_mu2

    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) *
                                                            (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()


def PSNR(pred, gt, shave_border=0):
    height, width = pred.shape[:2]
    pred = pred[shave_border:height - shave_border, shave_border:width - shave_border]
    gt = gt[shave_border:height - shave_border, shave_border:width - shave_border]
    imdff = pred - gt
    rmse = math.sqrt(np.mean(imdff ** 2))
    if rmse == 0:
        return 100
    return 20 * math.log10(255.0 / rmse)


def main():
    GT_path = "C:\\Users\\Tiger\\OneDrive - stu.scu.edu.cn\\Papers\\Mine\\Graduate\\figure\\chapter2\\Image_sets"
    Ours_path = "C:\\Users\\Tiger\\OneDrive - stu.scu.edu.cn\\Papers\\Mine\\Graduate\\figure\\chapter3\\perceptual\\" \
                "result\\lapsrn_rdn_div2k"
    LapSRN_path = "C:\\Users\\Tiger\\OneDrive - stu.scu.edu.cn\\Papers\\Mine\\Graduate\\figure\\chapter3\\perceptual" \
                  "\\result\\lapsrn"
    DRRN_path = "C:\\Users\\Tiger\\OneDrive - stu.scu.edu.cn\\Papers\\Mine\\Graduate\\figure\\chapter5\\perceptual" \
                  "\\result\\DRRN"

    box_size = 55
    step_size = 30
    image_set = 'Set14'
    start_point = 5

    image_path = GT_path+'\\'+image_set
    for image_name in os.listdir(image_path):
        print('Processing: ', image_name)
        GT = Image.open(GT_path + '\\' + image_set + '\\' + image_name).convert('RGB')
        GT = np.asanyarray(GT)
        Ours = Image.open(Ours_path + '\\' + image_set + '\\' + image_name).convert('RGB')
        Ours = np.asanyarray(Ours)
        LapSRN = Image.open(LapSRN_path + '\\' + image_set + '\\' + image_name).convert('RGB')
        LapSRN = np.asanyarray(LapSRN)
        DRRN = Image.open(DRRN_path + '\\' + image_set + '\\' + image_name).convert('RGB')
        DRRN = np.asanyarray(DRRN)

        best_diff_psnr = 0.0
        best_coor = [0, 0]
        for row_idx in np.arange(start_point, GT.shape[0]-box_size, step_size):
            for col_idx in np.arange(start_point, GT.shape[1]-box_size, step_size):
                row_end = row_idx+box_size
                col_end = col_idx+box_size
                GT_patch = GT[row_idx:row_end, col_idx:col_end, :]
                Ours_patch = Ours[row_idx:row_end, col_idx:col_end, :]
                LapSRN_patch = LapSRN[row_idx:row_end, col_idx:col_end, :]
                DRRN_patch = DRRN[row_idx:row_end, col_idx:col_end, :]
                Ours_psnr = SSIM(Ours_patch, GT_patch)
                LapSRN_psnr = SSIM(LapSRN_patch, GT_patch)
                DRRN_psnr = SSIM(DRRN_patch, GT_patch)

                diff_psnr = Ours_psnr-max(LapSRN_psnr, DRRN_psnr)
                if best_diff_psnr < diff_psnr:
                    best_diff_psnr = diff_psnr
                    best_coor[0] = row_idx
                    best_coor[1] = col_idx
        if best_diff_psnr == 0:
            print('Bad result!')
            continue
        row_idx = best_coor[0]
        col_idx = best_coor[1]
        row_end = row_idx + box_size
        col_end = col_idx + box_size
        patch = {
            'GT': GT[row_idx:row_end, col_idx:col_end, :],
            'DRRN': DRRN[row_idx:row_end, col_idx:col_end, :],
            'LapSRN': LapSRN[row_idx:row_end, col_idx:col_end, :],
            'Ours': Ours[row_idx:row_end, col_idx:col_end, :]
        }

        plt.figure(os.path.splitext(image_name)[0]+str([best_coor[1], best_coor[0]]))
        idx = 1
        for name in patch:
            plt.subplot(1, 4, idx)
            idx = idx+1
            plt.imshow(patch[name])
            plt.title(name)
            plt.axis('off')

        desk_path = r'C:\Users\Tiger\Pictures\idea3'
        fig_name = desk_path+'\\'+str([best_coor[1], best_coor[0]])+image_name
        plt.savefig(fig_name, dpi=300)
        # plt.show()
    a = 0


if __name__ == '__main__':
    main()

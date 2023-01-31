import torchvision
from PIL import Image
import numpy as np
import os
import cv2


def main():
    for i in range(0, 2):
        file_path = get_file_path(i)
        dst_path = get_dst_path(i)
        totentor = torchvision.transforms.ToTensor()
        color_aug = torchvision.transforms.ColorJitter(
            brightness=0.5, contrast=0.5, saturation=0.5, hue=0.1)
        color_jitter(file_path, dst_path, color_aug)


def get_dst_path(i):
    dst_path = ['D:/wp/DW_intern/high_img_color_jitter/', 'D:/wp/DW_intern/low_img_color_jitter/']
    return dst_path[i]


def get_file_path(i):
    file_path = ['D:/wp/DW_intern/synthesis_high_data/', 'D:/wp/DW_intern/synthesis_low_data/']
    return file_path[i]


def color_jitter(file_path, dst_root, color_aug):
    file_list = os.listdir(file_path)
    for ii in file_list:
        img = cv2.imread(file_path + ii)
        img = Image.fromarray(img)
        jitter_img = color_aug(img)
        rgb_jitter_img = cv2.cvtColor(np.array(jitter_img), cv2.COLOR_BGR2RGB)
        cv2.imwrite(dst_root + ii, rgb_jitter_img)


if __name__ == '__main__':
    main()

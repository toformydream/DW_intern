import cv2
import json
import numpy as np
import matplotlib as plt
import os


def main():
    # 배경, itme,
    img_number = 0
    json_data = load_json('D:/wp/DW_intern/json/synthesis_data.json')
    file_path = 'D:/wp/DW_intern/high_img_color_jitter'
    file_amount = get_filelist(file_path)
    item = ['item_0', 'item_1', 'item_2', 'item_3', 'item_4', 'item_5', 'item_6', 'item_7', 'item_8', 'item_9',
            'item_10', ]
    for i in range(file_amount):
        h, w = get_img_shape(file_path, i)
        mask = np.zeros((h, w), dtype=np.uint8)
        for j in range(0,10):
            img_name = f"{i}.png"
            item_seg = get_item_segmentation(json_data, img_number, j, img_name)
            item[j] = np.array(item_seg)
            print(item[j])
            # mask = drow_mask(mask, item[j], j)
        img_number = +1
        # plt.imshow(mask)


def drow_mask(mask, item, color):
    cv2.fillPoly(mask, [item], color)
    return mask


def load_json(json_path):
    with open(json_path, "r") as file:
        json_data = json.load(file)
    return json_data


def get_filelist(file_path):
    file = len(os.listdir(file_path))
    return file


def get_img_shape(file_path, img_path):
    img = cv2.imread(f"{file_path}/{img_path}.png")
    h, w = img.shape[:2]
    return h, w


#item_seg = get_item_segmentation(json_data, img_number, j, i)


def get_item_segmentation(json_data, img_number, item_number, img_name):
    item_seg = []
    item_seg = json_data['annotations'][img_number][img_name]['items'][item_number]['segmentation']['9'][0][0]
    return item_seg


# def save_mask(file_path):

if __name__ == '__main__':
    main()

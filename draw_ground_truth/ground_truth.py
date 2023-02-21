import cv2
import os
import json
import numpy as np
def main():
    json_path = 'C:/DW_intern-main/json/gun.json' ########################
    file_path = 'C:/DW_intern-main/gun_data_file' #################
    for i in range(len(file_path)):
        json_data = load_json(json_path)
        files_amount = files_count(file_path)
        for j in range(files_amount):
            img = cv2.imread(f"{file_path}/{j}.png")
            img_copy = img.copy()
            bbox = []

            h,w = img.shape[:2]
            seg = json_data['annotations'][j]['segmentation'][0][0]
            result = []
            for p in range(0, len(json_data['annotations'][j]['segmentation'][0][0]), 2):
                result.append(json_data['annotations'][j]['segmentation'][0][0][p:p + 2])
            vector = np.vectorize(np.int_)
            result = np.array(result)
            result = vector(result)
            for bbox_number in range(0, len(json_data['annotations'][j]['bbox'])):
                bbox.append(json_data['annotations'][j]['bbox'][bbox_number])
            img = cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 3)
            img_copy = cv2.fillPoly(img_copy, [result], (0, 0, 255))
            dst = cv2.addWeighted(img, 0.5, img_copy, 0.5, 0)
            cv2.imwrite(f"C:/DW_intern-main/gun_ground_truth/{j}.png", dst) ####################

def load_json(json_path):
    with open(json_path, 'r') as file:
        json_data = json.load(file)
    return json_data

def files_count(file_path):
    file_list = os.listdir(file_path)
    size = len(file_list)
    return size

if __name__ == '__main__':
    main()

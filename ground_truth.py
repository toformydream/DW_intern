import cv2
import json
import numpy as np
from mainn import files_count
from mainn import load_json
def main():
    json_path = 'json/gun_base_data.json'
    file_path = 'gun_data_file/'
    for i in range(len(file_path)):
        json_dic, json_data = load_json(json_path)
        files_amount = files_count(file_path)
        for j in range(files_amount):
            img = cv2.imread(file_path + f"{j}.png")
            img_copy = img.copy()
            bbox = []
            h,w = img.shape[:2]
            seg = json_data['annotations'][j]['segmentation'][0][0]
            result = []
            print(seg)
            for p in range(0, len(json_data['annotations'][j]['segmentation'][0][0]), 2):
                result.append(json_data['annotations'][j]['segmentation'][0][0][p:p + 2])
            print(result)
            vector = np.vectorize(np.int_)
            result = np.array(result)
            result = vector(result)
            for bbox_number in range(0, len(json_data['annotations'][j]['bbox'])):
                bbox.append(json_data['annotations'][j]['bbox'][bbox_number])
            img = cv2.fillPoly(img, [result], (0, 0, 255))
            img = cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 3)
            dst = cv2.addWeighted(img, 0.2, img_copy, 0.8, 0)
            cv2.imwrite('ground_truth_'+file_path + str(j)+'.png', dst)

if __name__ == '__main__':
    main()
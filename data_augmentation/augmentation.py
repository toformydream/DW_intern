import json
import cv2
import random
from make_train_data import file_amount
import os


def main():
    categories = ['knife', 'gun', 'battery', 'laser_pointer']
    json_list = 'C:/DW_intern-main/json/b/gun_base_data.json'  #########################
    file_list = 'C:/DW_intern-main/gun_data_file'  ############################
    # for li in range(len(file_list)):
    json_data = load_json(json_list)
    n = 0
    files_amount = file_amount(file_list)
    print(files_amount)
    while n < 9960:  # 데이터 만개 만들어
        for i in range(0, files_amount, 2):  #
            new_height = round(random.uniform(0.5, 1.5))  # 가로 세로 random 조정
            new_width = round(random.uniform(0.5, 1.5))
            for j in range(0, 2):  # high, low 비율 같게 해야함
                new_seg = []
                get_img = cv2.imread(f"{file_list}/{i + j}.png")# 원본 이미지 불러와서
                resize_img = cv2.resize(get_img, dsize=(0, 0), fx=new_width, fy=new_height,
                                        interpolation=cv2.INTER_LINEAR)
                cv2.imwrite(f"{file_list}/{files_amount + n}.png", resize_img)
                for seg_len in range(0, len(json_data['annotations'][i]['segmentation'][0][0])):
                    if seg_len % 2 == 0:
                        new_seg.append(json_data['annotations'][i]['segmentation'][0][0][seg_len] * new_width)
                    else:
                        new_seg.append(json_data['annotations'][i]['segmentation'][0][0][seg_len] * new_height)
                h, w, _ = resize_img.shape

                json_data['images'].append({  # json파일에서 image 부분 append
                    'id': files_amount + n,
                    'dataset_id': 1,
                    'path': 'D:/wp/DW_intern/' + file_list + str(files_amount + n) + '.png',
                    'file_name': str(files_amount + n) + '.png',
                    'width': w,
                    'height': h})
                json_data['annotations'].append({  # json파일에서 annotation 부분 append
                    'id': files_amount + n,
                    'image_id': files_amount + n,
                    'category_id': 1,
                    'bbox': [0, 0, w, h],
                    'segmentation': [[new_seg]],
                    'area': w * h,
                    'iscrowd': False,
                    'color': 'Unknown',
                    'unitID': 1,
                    'registNum': 1,
                    'number1': 4,
                    'number2': 4,
                    'weight': None})
                n = n + 1
    for q in range(len(categories)):
        json_data['categories'].append({
            'id': q + 1,
            'name': categories[q],
            'supercategory': 'item',
            'color': '040439',
            'metadata': ''})
    with open('C:/DW_intern-main/json/gun.json', 'w', encoding='utf-8') as file: ########################
        json.dump(json_data, file, indent=4)


def load_json(json_path):
    with open(json_path, 'r') as file:
        json_data = json.load(file)
    return json_data


if __name__ == '__main__':
    main()

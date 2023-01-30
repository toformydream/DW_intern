import random
import os
import cv2
import numpy as np
import json

'''
TODO
imwrite 부분이랑 갑자기 까맣게나옴 확인할것.
background.json까지 생성완료 합성된 사진에 background,item10개 json해서 업로드만 하면 끝!
'''
"""
1. 백그라운드 선택
2. 이미지 선택
3. 이미지 출력 및 정규화
4. 이미지 위치 선택
5. 합성
6. 2만번 반복 
:return:
"""


def main():
    synthesis_data = {}
    synthesis_data['images'] = []
    synthesis_data['annotations'] = []
    synthesis_data['categories'] = []
    synthesis_image_number = 0
    item_seg = {}
    name = ['knife','gun','laser_pointer','battery']
    for i in range(0,4):
        append_categories_json(synthesis_data,name,i)
    while synthesis_image_number < 10000:
        append_files_json(synthesis_data, synthesis_image_number)
        items, l_items, img_number, item_seg = get_ramdom_img(item_seg)  # item 이미지와 이미지 넘버를 담은리스트
        high_path, low_path = get_background_image() # 경로임
        high_background = cv2.imread(high_path)
        low_background = cv2.imread(low_path)
        high_background = normalize(high_background)
        low_background = normalize(low_background)
        h_b_h, h_b_w = high_background.shape[:2]
        l_b_h, l_b_w = low_background.shape[:2]
        append_background_json(synthesis_data, synthesis_image_number, h_b_w, h_b_h)  # TODO
    #     # 위에서 랜덤값 지정 두번돌아가지 않도록
        for item_number in range(0, 10):
            high_img = cv2.imread(items[item_number])  # item 10개 각각 img로
            low_img = cv2.imread(l_items[item_number])
            h_x, h_y, h_h, h_w = get_random_coordinate(high_img, h_b_h, h_b_w)
            l_x, l_y, l_h, l_w = get_random_coordinate(low_img, l_b_h, l_b_w)   # x,y는 시작점 좌표, h,w 는 item이미지의 높이와 너비
            normalized_high_image = normalize(high_img)
            normalized_low_image = normalize(low_img)
            for c_x in range(h_x, h_x + h_w):
                for c_y in range(h_y, h_y + h_h):
                    high_background[c_y][c_x] = high_background[c_y][c_x] * normalized_high_image[c_y - h_y][c_x - h_x]

            for c_x in range(l_x, l_x + l_w):
                for c_y in range(l_y, l_y + l_h):
                    low_background[c_y][c_x] = low_background[c_y][c_x] * normalized_low_image[c_y -l_y][c_x - l_x]
            append_items_json(synthesis_data, synthesis_image_number, item_number, l_x, l_y, l_w, l_h, item_seg)
        cv2.imwrite(f"synthesis_high_data/{synthesis_image_number}.png", high_background*256)
        cv2.imwrite(f"synthesis_low_data/{synthesis_image_number}.png", low_background*256)
        print(synthesis_image_number)
        synthesis_image_number += 1
    with open('json/synthesis_data.json', 'w', encoding='utf-8') as file:
        json.dump(synthesis_data, file, indent=4)


def append_files_json(synthesis_data, synthesis_image_number):
    synthesis_data['images'].append({
        f"{synthesis_image_number}.png" : {
            'background' : [],
            'items' : []
        }


    })
    synthesis_data['annotations'].append({
        f"{synthesis_image_number}.png" : {
            'items' : []
        }

    })
def append_background_json(synthesis_data, synthesis_image_number, b_w, b_h):
    synthesis_data['images'][synthesis_image_number][f"{synthesis_image_number}.png"]['background'].append({
                        'id': synthesis_image_number,
                        'dataset_id': '',
                        'path': f"D:/wp/DW_intern/synthesis_high_data/{synthesis_image_number}.png",
                        'file_name': f"{synthesis_image_number}.png",
                        'width': b_w,
                        'height': b_h
    })
    return synthesis_data

def append_categories_json(synthesis_data,name,i):
    synthesis_data['categories'].append({
        'id' : i+1,
        'name' : name[i],
        'supercategory' : '',
        'color' : '',
        'metatdata' : ''
    })
def append_items_json(synthesis_data, sysnthesis_image_number, item_number, x, y, w, h, item_seg):
    synthesis_data['images'][sysnthesis_image_number][f"{sysnthesis_image_number}.png"]['items'].append({
            'id': f"{sysnthesis_image_number}-{item_number}",
            'dataset_id': '',
            'path': f"D:/wp/DW_intern/synthesis_high_data/{sysnthesis_image_number}.png",
            'file_name': f"{sysnthesis_image_number}.png",
            'width': w,
            'height': h
    })
    synthesis_data['annotations'][sysnthesis_image_number][f"{sysnthesis_image_number}.png"]['items'].append({
            'id': f"{sysnthesis_image_number}-{item_number}",
            'category_id': '',
            'bbox': [x, y, x + w, x + h],
            'segmentation': item_seg,
            'area': w * h,
            'iscrowd': '',
            'color' : '',
            'unitID' : '',
            'registNum' : '',
            'number1' : '',
            'number2' : '',
            'weight' : ''
    })
    return synthesis_data



def load_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    return json_data


def normalize(image):
    image = image / 65535
    normalized_image = cv2.normalize(image, None, 0, 1, cv2.NORM_MINMAX)
    return normalized_image


def get_background_image():
    count = random.randrange(1, 5)
    high_img = f"background/high_{count}.png"
    low_img = f"background/low_{count}.png"
    return high_img, low_img


def get_random_coordinate(img, b_h, b_w):
    h, w = img.shape[:2]
    new_x = round(random.uniform(0, b_w - w))
    new_y = round(random.uniform(0, b_h - h))
    return new_x, new_y, h, w,


def get_ramdom_img(item_seg):
    json_data = ['gun_json', 'battery_json', 'knife_json', 'laser_json']
    data_files = ['ground_truth_gun_data_file', 'ground_truth_battery_data_file', 'ground_truth_knife_data_file',
                  'ground_truth_laser_point_data_file']
    for i in range(4):
        json_data[i] = load_json('json/' + data_files[i] + '.json')
    h_items = []
    l_items = []
    file_numbers = []
    for i in range(0, 10):
        file = random.randrange(0, 4)
        files = data_files[file]
        file_number = random.randrange(0, 10000, 2)
        item_seg = {i: json_data[file]['annotations'][file_number]['segmentation']}
        file_numbers.append(file_number)
        h_items.append(files + f"/{file_number}.png")
        l_items.append(files + f"/{file_number + 1}.png")
    return h_items, l_items, file_numbers, item_seg


if __name__ == '__main__':
    main()

import random
import os
import cv2
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
    while synthesis_image_number < 10000:
        items, l_items, img_number, item_seg = get_ramdom_img(item_seg)  # item 이미지와 이미지 넘버를 담은리스트
        high_path, low_path = get_background_image()
        background_list = [high_path, low_path]
        # append_background_json(synthesis_data, synthesis_image_number, b_w, b_h)  # TODO : 랜덤으로 x,y좌표를 정해주는 코드를 두번 돌아가지 않도록, 10번 반복해서 2중 배열로 [0][x,y..]/[1][x,y..] 형태로 만들기
        '''random_coordinate=[[6]]
        background = cv2.imread(background_list[0])
        for imgs in range(len(items)):
            img = cv2.imread(items[imgs])  # item 10개 각각 img로
            x, y, h, w, b_h, b_w = get_random_coordinate(img, background)
            random_coordinate[imgs] = x,y,h,w,b_h,b_w
        print(random_coordinate)
        '''
        for i in range(0, 2):
            background = cv2.imread(background_list[i])
            background = normalize(background)
            for item_number in range(0, 10):
                if i == 1:
                    items[item_number] = l_items[item_number]
 # x,y는 시작점 좌표, h,w 는 item이미지의 높이와 너비
                normalized_image = (normalize(img))
                # append_items_json(synthesis_data, sysnthesis_image_number, item_number,x,y,w,h,item_seg)
                for c_x in range(x, x + w):
                    for c_y in range(y, y + h):
                        background[c_y][c_x] = background[c_y][c_x] * normalized_image[c_y - y][c_x - x]
            if i == 0:
                cv2.imwrite(f"synthesis_high_data/{synthesis_image_number}.png", background)  # imwrite로 바꾸고 경로설정 다르게
                cv2.imshow('h', background)
            else:
                cv2.imwrite(f"synthesis_low_data/{synthesis_image_number}.png", background)
                cv2.imshow('l', background)
                append_items_json(synthesis_data, synthesis_image_number, item_number, x, y, w, h, item_seg)
        print(synthesis_image_number)
        synthesis_image_number += 1
        cv2.waitKey()
    with open('json/synthesis_data.json', 'w', encoding='utf-8') as file:
        json.dump(synthesis_data, file, indent=4)


def normalize_background(background_list):
    background = cv2.imread(background_list)
    background = normalize(background)
    return background


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


def get_random_coordinate(img, background):
    b_h, b_w = background.shape[:2]
    h, w = img.shape[:2]
    new_x = round(random.uniform(0, b_w - w))
    new_y = round(random.uniform(0, b_h - h))
    # print(b_h,b_w,h, w,new_x,new_y)
    return new_x, new_y, h, w, b_h, b_w


def get_ramdom_img(item_seg):
    json_data = ['gun_json', 'battery_json','knife_json','laser_json']
    data_files = ['ground_truth_gun_data', 'ground_truth_battery_data', 'ground_truth_knife_data',
             'ground_truth_laser_point_data']
    for i in range(4):
        json_data[i] = load_json('json/'+data_files[i]+'.json')
    h_items = []
    l_items = []
    file_numbers = []
    for i in range(0, 10):
        file = random.randrange(0,4)
        files = data_files[file]
        file_number = random.randrange(0, 10000, 2)
        item_seg = {i: json_data[file]['annotations'][file_number]['segmentation']}
        file_numbers.append(file_number)
        h_items.append(files + f"/{file_number}.png")
        l_items.append(files + f"/{file_number + 1}.png")
    return h_items, l_items, file_numbers, item_seg


def append_background_json(synthesis_data, synthesis_image_number, b_w, b_h):
    synthesis_data['images'].append({
        'background' : {'id': synthesis_image_number,
        'dataset_id': '',
        'path': f"D:/wp/DW_intern/synthesis_high_data/{synthesis_image_number}.png",
        'file_name': f"{synthesis_image_number}.png",
        'width': b_w,
        'height': b_h},

    })
    return synthesis_data


def append_items_json(synthesis_data, sysnthesis_image_number, item_number, x, y, w, h, item_seg):
    synthesis_data['images'].append({
        'items' : {
        'id': f"{sysnthesis_image_number}-{item_number}",
        'dataset_id': '',
        'path': f"D:/wp/DW_intern/synthesis_high_data/{sysnthesis_image_number}.png",
        'file_name': f"{sysnthesis_image_number}.png",
        'width': w,
        'height': h}
    })
    synthesis_data['annotations'].append({
        'items' : {'id': f"{sysnthesis_image_number}-{item_number}",
        'category_id': '',
        'bbox': [x, y, x + w, x + h],
        'segmentation': item_seg,
        'area': w * h,
        'iscrowd': ''}
    })
    return synthesis_data


if __name__ == '__main__':
    main()

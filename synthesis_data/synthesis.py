import random
import cv2
import json

"""
1. 백그라운드 선택
2. 이미지 선택
3. 이미지 출력 및 정규화
4. 이미지 위치 선택
5. 합성
6. 2만번 반복 
"""


def main():
    synthesis_data = {}
    synthesis_data['images'] = []
    synthesis_data['annotations'] = []
    synthesis_data['categories'] = []
    synthesis_image_number = 0
    json_item_number = 0
    item_seg = {}
    name = ['knife', 'gun', 'laser_pointer', 'battery']
    for i in range(0, 4):
        append_categories_json(synthesis_data, name, i)
    while synthesis_image_number <10000:
        items, l_items, img_number, item_seg, category_id, iscrowd, color, unitID, registNum, number1, number2, weight = get_ramdom_img(item_seg)  # item 이미지와 이미지 넘버를 담은리스트
        high_path, low_path = get_background_image() # 경로임
        high_background = normalize(high_path)
        low_background = normalize(low_path)
        h_b_h, h_b_w = high_background.shape[:2]
        l_b_h, l_b_w = low_background.shape[:2]
        append_files_json(synthesis_data, synthesis_image_number, h_b_w, h_b_h)  # TODO
    #     # 위에서 랜덤값 지정 두번돌아가지 않도록
        for item_number in range(0, 10):
            segmentation = []
            x_seg = []
            y_seg = []
            po = []
            a = []
            for seg_element in range(len(item_seg)):
                po = item_seg[seg_element]
                a = po[0][0]
                x_seg.append(a[::2])
                y_seg.append(a[1::2])
            high_img = cv2.imread(items[item_number])  # item 10개 각각 img로
            low_img = cv2.imread(l_items[item_number])
            h_x, h_y, h_h, h_w = get_random_coordinate(high_img, h_b_h, h_b_w)
            l_x, l_y, l_h, l_w = get_random_coordinate(low_img, l_b_h, l_b_w)   # x,y는 시작점 좌표, h,w 는 item이미지의 높이와 너비
            normalized_high_image = normalize(high_img)
            normalized_low_image = normalize(low_img)
            a = (len(x_seg[item_number]))
            # print(x_seg[item_number])
            # print('====================================================================================')
            x_seg = add_x_y(x_seg[item_number], h_x, a)
            # print(x_seg[item_number])
            y_seg = add_x_y(y_seg[item_number], h_y, a)
            segmentation = combine_seg(segmentation, x_seg, y_seg)
            for c_x in range(h_x, h_x + h_w):
                for c_y in range(h_y, h_y + h_h):
                    high_background[c_y][c_x] = high_background[c_y][c_x] * normalized_high_image[c_y - h_y][c_x - h_x]
            for c_x in range(h_x, h_x + l_w):
                for c_y in range(h_y, h_y + l_h):
                    low_background[c_y][c_x] = low_background[c_y][c_x] * normalized_low_image[c_y -h_y][c_x - h_x]
            append_items_json(synthesis_data,synthesis_image_number,h_x, h_y, l_w, l_h, segmentation , json_item_number,category_id, iscrowd, color, unitID, registNum, number1, number2, weight)
            json_item_number = json_item_number+1
        cv2.imwrite(f"C:/DW_intern-main/high_synthesis/{synthesis_image_number}.png", high_background*256)
        cv2.imwrite(f"C:/DW_intern-main/low_synthesis/{synthesis_image_number}.png", low_background*256)
        print(synthesis_image_number)
        synthesis_image_number += 1
    with open('C:/DW_intern-main/json/synthesis.json', 'w', encoding='utf-8') as file:
        json.dump(synthesis_data, file, indent=4)


def combine_seg(seg, x_seg, y_seg):
    for i in range(len(x_seg)):
        seg.append(x_seg[i])
        seg.append(y_seg[i])
    return seg


def add_x_y(seg, x_y, a):
    for i in range(a):
        # print(i)
        seg[i] = seg[i] + x_y

    return seg


def append_files_json(synthesis_data, synthesis_image_number, b_w, b_h):
    synthesis_data['images'].append({
        'id': synthesis_image_number,
        'dataset_id': '',
        'path': f"C:/DW_intern-main/high_synthesis/{synthesis_image_number}.png",
        'file_name': f"{synthesis_image_number}.png",
        'width': b_w,
        'height': b_h
    })
    return synthesis_data

def append_categories_json(synthesis_data, name, i):
    synthesis_data['categories'].append({
        'id': i + 1,
        'name': name[i],
        'supercategory': 'item',
        'color': '040439',
        'metatdata': ''
    })


def append_items_json(synthesis_data,synthesis_image_number, x, y, w, h,
                      seg,json_item_number,category_id, iscrowd, color, unitID, registNum, number1, number2, weight):
    synthesis_data['annotations'].append({
        'id': json_item_number,
        'image_id' : synthesis_image_number,
        'category_id': category_id,
        'bbox': [x, y, x + w, y + h],
        'segmentation': seg,
        'area': w * h,
        'iscrowd': iscrowd,
        'color': color,
        'unitID': unitID,
        'registNum': registNum,
        'number1': number1,
        'number2': number2,
        'weight': weight
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
    count = random.randrange(1,5)
    high_img = cv2.imread(f"C:/DW_intern-main/background/high_{count}.png")
    low_img = cv2.imread(f"C:/DW_intern-main/background/low_{count}.png")
    resize_high = cv2.resize(high_img, dsize=(700,700), interpolation = cv2.INTER_AREA)
    resize_low = cv2.resize(low_img, dsize=(700, 700), interpolation=cv2.INTER_AREA)
    return resize_high,resize_low


def get_random_coordinate(img, b_h, b_w):
    h, w = img.shape[:2]
    new_x = round(random.uniform(0, b_w - w-100))
    new_y = round(random.uniform(0, b_h - h-100))
    return new_x, new_y, h, w,


def get_ramdom_img(item_seg):
    json_data = ['gun_json', 'battery_json', 'knife_json', 'laser_json']
    json_path = ['gun','battery','knife','laser']
    data_files = ['gun_data_file', 'battery_data_file', 'knife_data_file',
                  'laser_data_file']
    for i in range(4):
        json_data[i] = load_json(f"C:/DW_intern-main/json/{json_path[i]}.json")
    h_items = []
    l_items = []
    file_numbers = []
    for i in range(0, 10):
        file = random.randrange(0, 4)
        files = data_files[file]
        file_number = random.randrange(0, 9900, 2)
        category_id = json_data[file]['annotations'][file_number]['category_id']
        item_seg[i] = json_data[file]['annotations'][file_number]['segmentation']
        iscrowd = json_data[file]['annotations'][file_number]['iscrowd']
        color = json_data[file]['annotations'][file_number]['color']
        unitID = json_data[file]['annotations'][file_number]['unitID']
        registNum = json_data[file]['annotations'][file_number]['registNum']
        number1 = json_data[file]['annotations'][file_number]['number1']
        number2 = json_data[file]['annotations'][file_number]['number2']
        weight = json_data[file]['annotations'][file_number]['weight']
        file_numbers.append(file_number)
        h_items.append(f"C:/DW_intern-main/{files}/{file_number}.png")
        l_items.append(f"C:/DW_intern-main/{files}/{file_number + 1}.png")
    return h_items, l_items, file_numbers, item_seg, category_id, iscrowd, color, unitID, registNum, number1, number2, weight


if __name__ == '__main__':
    main()

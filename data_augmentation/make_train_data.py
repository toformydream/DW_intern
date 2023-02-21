import json
import cv2
import os
import re
def main():
    img_amount = 0
    categories = ['knife', 'gun', 'battery', 'laser_point']
    file_path = ['gas_gun','toy_gun'] ######################
    data = {}
    data['images'] = []
    data['annotations'] = []
    data['categories'] = []

    for num in range(len(file_path)):
        sorted_dic = {}
        file_size = file_amount(f"C:/DW_intern-main/{file_path[num]}")
        json_data, json_dic = load_json(f"C:/DW_intern-main/json/a/{file_path[num]}.json",file_size)
        print(json_dic)
        print(sorted(json_dic.items()))
        sorted_dic = dict(sorted(json_dic.items()))
        for i in range(0, 20):

            print(file_path[num]+"/" + str(i) + '.png')
            img = cv2.imread(f"C:/DW_intern-main/{file_path[num]}/{i}.png")
            cv2.imwrite(f"C:/DW_intern-main/gun_data_file/{str(i + img_amount)}.png", img)######################
            print(json_dic[i])
            data['images'].append({  # json파일에서 image 부분 append
                'id': i + img_amount,
                'dataset_id': 1,
                'path': 'D:/wp/DW_intern/knife_data_file' + str(i + img_amount) + '.png',
                'file_name': str(i + img_amount) + '.png',
                'width': json_data['images'][int(json_dic[i])]['width'],
                'height': json_data['images'][int(json_dic[i])]['height']})
            data['annotations'].append({  # json파일에서 annotation 부분 append
                'id': i + img_amount,
                'image_id': i + img_amount,
                'category_id': 1,
                'bbox': json_data['annotations'][int(json_dic[i])]['bbox'],
                'segmentation': json_data['annotations'][int(json_dic[i])]['segmentation'],
                'area': json_data['annotations'][int(json_dic[i])]['area'],
                'iscrowd':  json_data['annotations'][int(json_dic[i])]['iscrowd'],
                'color':  json_data['annotations'][int(json_dic[i])]['color'],
                'unitID':  json_data['annotations'][int(json_dic[i])]['unitID'],
                'registNum':  json_data['annotations'][int(json_dic[i])]['registNum'],
                'number1':  json_data['annotations'][int(json_dic[i])]['number1'],
                'number2':  json_data['annotations'][int(json_dic[i])]['number2'],
                'weight':  json_data['annotations'][int(json_dic[i])]['weight']})
        img_amount = img_amount + 20
    for q in range(len(categories)):
        data['categories'].append({
            'id': q + 1,
            'name': categories[q],
            'supercategory': 'item',
            'color': '040439',
            'metadata': ''})
        print(len(data))

    with open('C:/DW_intern-main/json/b/gun_base_data.json', 'w', encoding='utf-8') as file: #######################
        json.dump(data, file, indent=4)

def file_amount(file_path):
    file_list = os.listdir(file_path)
    size = len(file_list)
    return size


def load_json(json_path, size):
    json_dic = {}
    with open(json_path, 'r') as file:
        json_data = json.load(file)
    for i in range(0,size):
        j = int(re.sub(r'[^0-9]', '', json_data['images'][i]['file_name']))
        json_dic[j] = i

    return json_data, json_dic


if __name__ == '__main__':
    main()


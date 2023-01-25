import os
import json
import cv2
from collections import OrderedDict
from mainn import files_count
from mainn import amend_json
from mainn import load_json

def main():
    img_amount = 0
    categories = ['knife', 'gun','bettery','laser_point']
    file_path = ['art_knife','chief_knife','fruit_knife','jack_knife','office_knife','steak_knife','swiss_army_knife']
    data = {}
    data['images'] = []
    data['annotations'] = []
    data['categories'] = []
    for num in range(len(file_path)):
        json_dic, json_data = load_json('json/'+file_path[num] + '.json')
        print(json_data)
        print(json_dic)
        for i in range(0,20):
            # print(file_path[num]+"/" + str(i) + '.png')
            img = cv2.imread(file_path[num]+"/" + str(i) + '.png')
            cv2.imwrite('knife_data_file/' + str(i+img_amount) + '.png', img)
            data['images'].append({  # json파일에서 image 부분 append
                'id': i+img_amount,
                'dataset_id': 1,
                'path': 'D:/wp/DW_intern/knife_data_file'+str(i+img_amount) + '.png',
                'file_name': str(i+img_amount) + '.png',
                'width': json_data['images'][json_dic[str(i)+'.png']]['width'],
                'height': json_data['images'][json_dic[str(i)+'.png']]['height']})
            data['annotations'].append({  # json파일에서 annotation 부분 append
                'id': i+img_amount,
                'image_id':i+img_amount,
                'category_id': 1,
                'bbox': json_data['annotations'][json_dic[str(i)+'.png']]['bbox'],
                'segmentation': json_data['annotations'][json_dic[str(i)+'.png']]['segmentation'],
                'area': json_data['annotations'][json_dic[str(i)+'.png']]['area'],
                'iscrowd': False,
                'color': 'Unknown',
                'unitID': 1,
                'registNum': 1,
                'number1': 4,
                'number2': 4,
                'weight': None})
        img_amount = img_amount + 20
    for q in range(len(categories)):
        data['categories'].append({
            'id' : q+1,
            'name': categories[q],
            'supercategory' : 'item',
            'color' : '040439',
            'metadata' : '' })


        print(len(data))
    with open('json/knife_base_data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)




if __name__ == '__main__':
    main()
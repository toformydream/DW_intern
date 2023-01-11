import cv2
import random
import os
import json
def main():
    load_json('crop_art_knife_2')

def load_json(json_path): #json파일 불러오기 # 딕셔너리[file number : json number] 생성
    json_dic = {}

    with open(json_path) as file: #json파일 열기
        json_data = json.load(file)

    for json_number in range(len(json_data['images'])): #이미지 안에 파일명, json 번호로 딕셔너리 만들기기
        json_dic[json_data['images'][json_number]['file_name']]=json_number

    return json_dic, json_data


def sort_json_file(json_dic = {}):
    json_dic.sort(key=len)
    sorted("json_dic")
    return json_dic

# def resize_file(file_path):
#     og_img = cv2.imread(file_path)
#     for
#     new_height = round(random.uniform(0.5,2))
#     new_width = round(random.uniform(0,5,2))

if __name__ == "__main__":
    main()

# def files_count(folder_path):
#     dirListing = os.listdir(folder_path)
#     return len(dirListing)
# print(augm_json_train['images']) # 제대로 불러왔는지 확인
#
# files_amount = files_count('crop_art_knife_2')
# print(files_amount)
# # for j in range(0,files_amount):
# #     print(j)
# #     print(len(augm_json_train['annotations'][j]['segmentation'][0][0]))
# plus_number=0
# for j in range(0, files_amount, 2): # 0.png부터 순차적으로 하나씩
#     for i in range(0,3): # png파일하나당 3개씩 만들기
#         new_height = random.uniform(0.5, 2)  # 가로 세로 random 조정
#         new_width = random.uniform(0.5, 2)
#         new_height = round(new_height, 2)
#         new_width = round(new_width, 2)
#         for resize in range(1,3):# high 이미지와 low 이미지 같은 비율로 resize
#             if resize == 1:
#                 new_seg = []
#                 get_img = cv2.imread('crop_art_knife_2/'+str(j)+'.png')
#                 resize_high_img = cv2.resize(get_img, dsize=(0, 0), fx=new_width, fy=new_height, interpolation=cv2.INTER_LINEAR)
#                 for seg_len in range(0,len(augm_json_train['annotations'][j]['segmentation'][0][0])):
#                     if seg_len % 2 == 0:
#                         new_seg.append(augm_json_train['annotations'][j]['segmentation'][0][0][seg_len] * new_width)
#                     else:
#                         new_seg.append(augm_json_train['annotations'][j]['segmentation'][0][0][seg_len] * new_height)
#                 cv2.imwrite('crop_art_knife_2/' + str(files_amount+plus_number) + '.png', resize_high_img)
#                 new_img = cv2.imread('crop_art_knife_2/' + str(files_amount+plus_number) + '.png')
#                 h, w ,c= new_img.shape
#                 augm_json_train['images'].append({  # json파일에서 image 부분 append
#                     'id': files_amount+plus_number,
#                     'dataset_id': 1,
#                     'path': 'D:/KJE_Airiss/Police_data/xray/data/xray_artknife_a_2/crop/' + str(files_amount+plus_number) + '.png',
#                     'file_name': str(files_amount+plus_number) + '.png',
#                     'width': w,
#                     'height': h})
#                 augm_json_train['annotations'].append({  # json파일에서 annotation 부분 append
#                     'id': files_amount+plus_number+ 1,
#                     'image_id': files_amount+plus_number + 1,
#                     'category_id': 1,
#                     'bbox': [0, 0, w,h],
#                     'segmentation': [[new_seg]],
#                     'area': h * w,
#                     'iscrowd': False,
#                     'color': 'Unknown',
#                     'unitID': 1,
#                     'registNum': 1,
#                     'number1': 4,
#                     'number2': 4,
#                     'weight': None})
#                 plus_number += 1
#             else:
#                 get_img = cv2.imread('crop_art_knife_2/' + str(j+1) + '.png')
#                 new_seg = []
#                 resize_high_img = cv2.resize(get_img, dsize=(0, 0), fx=new_width, fy=new_height,
#                                              interpolation=cv2.INTER_LINEAR)
#                 cv2.imwrite('crop_art_knife_2/' + str(files_amount + plus_number) + '.png', resize_high_img)
#                 new_img = cv2.imread('crop_art_knife_2/' + str(files_amount + plus_number) + '.png')
#                 h, w, c = new_img.shape
#                 for seg_len in range(0, len(augm_json_train['annotations'][j]['segmentation'][0][0])):
#                     if seg_len % 2 == 0:
#                         new_seg.append(augm_json_train['annotations'][j]['segmentation'][0][0][seg_len] * new_width)
#                     else:
#                         new_seg.append(augm_json_train['annotations'][j]['segmentation'][0][0][seg_len] * new_height)
#                 augm_json_train['images'].append({  # json파일에서 image 부분 append
#                     'id': files_amount + plus_number,
#                     'dataset_id': 1,
#                     'path': 'D:/KJE_Airiss/Police_data/xray/data/xray_artknife_a_2/crop/' + str(files_amount + plus_number) + '.png',
#                     'file_name': str(files_amount + plus_number) + '.png',
#                     'width': w,
#                     'height': h})
#
#                 augm_json_train['annotations'].append({  # json파일에서 annotation 부분 append
#                     'id': files_amount + plus_number + 1,
#                     'image_id': files_amount + plus_number + 1,
#                     'category_id': 1,
#                     'bbox': [0, 0, w, h],
#                     'segmentation':[[new_seg]],
#                     'area': h * w,
#                     'iscrowd': False,
#                     'color': 'Unknown',
#                     'unitID': 1,
#                     'registNum': 1,
#                     'number1': 4,
#                     'number2': 4,
#                     'weight': None})
#                 plus_number += 1
#
# with open(json_root, "w", encoding="UTF-8") as file:  # pc : poice
#     json.dump(augm_json_train, file, indent=4)


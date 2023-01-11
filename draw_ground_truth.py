import cv2
import numpy as np
import json
import os
import operator
json_root = 'json/crop_data.json'
with open(json_root, "r", encoding="UTF-8") as file:  # pc : poice # json파일 불러오기
    augm_json_train = json.load(file)
green_color = (0,255,0)
def files_count(folder_path): #파일 갯수 카운트
    dirListing = os.listdir(folder_path)
    return len(dirListing)

def list_chunk(lst, n): # 리스트 분할
    return [lst[i:i+n] for i in range(0, len(lst), n)]
# print(augm_json_train['images']) # 제대로 불러 왔는지 확인

files_amount = files_count('crop_art_knife_2')
files_amount = files_amount-1
print(files_amount)
key_dic=[]
value_dic=[]
new_dic={}
file_json_dic={}
for file_numbers in range(0,files_amount):
    print(str('crop_art_knife_2/'+str(file_numbers)+'.png'))
    file_json_dic[file_numbers] = str(file_numbers)+'.png'
    key_dic.append(augm_json_train['images'][file_numbers]['file_name'])
for k in sorted(file_json_dic, key=len):
    file_json_dic[k] = file_json_dic[k]
key_dic.sort(key=len)
for i in range(len(alist)):
    file_json_dic[i] = alist[i]
print(file_json_dic)


# file_json_dic.sort(key=len)
# for file_number in range(files_amount):
#
#     img = cv2.imread('crop_art_knife_2/' + str(files_amount) + '.png')
#     bbox = []
#     h,w,c = img.shape
#     seg = augm_json_train['annotations'][file_number]['segmentation'][0][0]
#     result = []
#     for i in range(0, len(augm_json_train['annotations'][file_number]['segmentation'][0][0]), 2):
#         result.append(augm_json_train['annotations'][file_number]['segmentation'][0][0][i:i + 2])
#     print(modify_list)
#     vector = np.vectorize(np.int_)
#     result = np.array(result)
#     result = vector(result)
#     # print(type(result))
#     print(result)
#     for bbox_number in range(0,len(augm_json_train['annotations'][file_number]['bbox'])): #ㅠㅠㅔ
#         bbox.append(augm_json_train['annotations'][file_number]['bbox'][bbox_number])
#     print(bbox)
#     img = cv2.fillPoly(img,[result],(0,0,255))
#     img = cv2.rectangle(img, (bbox[0],bbox[1]), (bbox[2],bbox[3]),green_color,3)
#     cv2.imshow('ing', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
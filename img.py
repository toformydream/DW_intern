import numpy
import json
import cv2
json_root = "D:\\wp\\testcase\\venv\\crop_art_knife_2\\crop_data.json"


with open(json_root, "r", encoding="UTF-8") as file:  # pc : poice
    augm_json_train = json.load(file)

print(len(augm_json_train['images']))
print(augm_json_train['annotations'][86])
print(augm_json_train['categories'])
#
# imgimg=86
# augm_json_train_new = {'images': [], 'annotations': []}
# img_annot_id_new = 86
# img_id_new = 86
# for i in range(258):
#     img = cv2.imread('venv/crop_art_knife_2/' + str(imgimg) + '.png')
#     h, w, c = img.shape
#     boundbox = [0, 0, w, h]
#     json_new_annotation = []
#
#     json_new_images = {
#         'id': img_id_new,
#         'dataset_id': 1,
#         'path': 'synthesis_'+str(imgimg)+'.png',
#         'file_name': 'synthesis_'+str(imgimg)+'.png',
#         'width': w,
#         'height': h}
#     (augm_json_train['images']).append(json_new_images)
#     img_id_new = img_id_new+1
#
#     json_new_annotation = {
#         'id': i+86,
#         'image_id': i+86,
#         'category_id': 1,
#         'bbox': boundbox,
#         'segmentation':0,
#         'area': h*w,
#         'iscrowd': False,
#         'color': 'Unknown',
#         'unitID': 1,
#         'registNum': 1,
#         'number1': 4,
#         'number2': 4,
#         'weight': None}
#     augm_json_train['annotations'].append(json_new_annotation)
#     img_annot_id_new = img_annot_id_new+1

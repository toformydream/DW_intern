import numpy
import json
json_root='venv/crop_art_knife_2/crop_data.json'

with open(json_root,"r") as pc_train_json:  # pc : poice
    augm_json_train = json.load(pc_train_json)

print(len(augm_json_train['images']))
print(augm_json_train['annotations'][85])
print(augm_json_train['categories'])

augm_json_train_new={'images':[],'annotations':[]}
img_annot_id_new=max(augm_json_train['annotations'])
img_id_new=augm_json_train['image'][85]+1
for i in range(258):
            json_new_annotation=[]

            json_new_annotation=  {'id': i+86,
            'image_id': i+86,
            'category_id': 1,
            'bbox': bbox_item1,
            'segmentation':segm1,                    
            'area':area,
            'iscrowd': False,
            'color': 'Unknown',
            'unitID': 1,
            'registNum': 1,
            'number1': 4,
            'number2': 4,
            'weight': None}
            augm_json_train_new['annotations'].append(json_new_annotation)
            img_annot_id_new=img_annot_id_new+1



            json_new_images= {'id': img_id_new,
                       'dataset_id': 1,
                       'path': 'synthesis_'+str(imgimg)+'.png',
                       'file_name': 'synthesis_'+str(imgimg)+'.png',
                       'width': bg_w,
                       'height':bg_h}
            augm_json_train_new['images'].append(json_new_images)
            img_id_new=img_id_new+1

'''
1. json 파일 불러오기 o
2. json파일순서와 이미지 파일이 순서대로 되게끔 설정
3. 이미지 3개씩 resize o
4. resize 이미지 json파일에 데이터 업로드 o
5. bbox, segmentation 이미지에 만들기
6. 각각의 json파일, 폴더에서 3배로 resize하고 하나의 json파일, 하나의 폴더에 에 ground_truth만 저장하는 방식, json파일 합쳐야함
신경써야할 부분은
{1. ground_truth될 파일이나 json id로 업로드 될 숫자들이 잘 갱신 되는지}
'''
import json
import cv2
import numpy as np
import random
import os
import natsort


def main():
    file_list = ['art_knife', 'chief_knife', 'fruit_knife', 'jack_knife', 'steak_knife','swiss_army_knife']
    img_amount = 0
    for i in range(0,6):
        files = files_count(str(file_list[i]))
        json_dic, json_data = load_json('json/' + str(file_list[i]) + '.json')
        folder_path = find_folder_path(str(file_list[i]))
        resize_upload_image(str(file_list[i]), json_data, json_dic, img_amount)
        json_dic, json_data = load_json('json/'+str(file_list[i])+'.json')
        draw_ground_truth(file_list[i], json_data, json_dic)

def find_folder_path(path):
    a = ('json/'+str(path)+'.json')
    return a

def files_count(folder_path):  # 파일 갯수 카운트
    file_amount = os.listdir(folder_path)
    return len(file_amount)


def load_json(json_path):  # json파일 불러오기 # 딕셔너리[file number : json number] 생성
    json_dic = {}
    with open(json_path, "r") as file:  # json파일 열기
        json_data = json.load(file)
    for json_number in range(len(json_data['images'])):  # 이미지 안에 파일명, json 번호로 딕셔너리 만들기기
        json_dic[json_data['images'][json_number]['file_name']] = json_number
    return json_dic, json_data


def load_imgs(imgs_path):
    img_list = os.listdir(imgs_path)
    sorted_img_list = natsort.natsorted(img_list)
    return sorted_img_list

def combine_json(json_1_path, json_2_path): #큰게 앞으로
    with open(json_1_path, "r") as file:
        json_1_data = json.load(json_1_path)
    with open(json_2_path, "r") as file:
        json_2_data = json.load(json_2_path)
    json_1_data.update(json_2_data)
    return json_1_data







new_height = new_width = 0


def resize_upload_image(file_path, json_data, json_dic, img_amount): # folder_path, json_data, json_dic, img_amount
    global new_height
    global new_width
    files_amount = files_count(file_path)
    plus_number = 0
    img_list = load_imgs(file_path)
    for j in range(0, files_amount,2):  # 0.png부터 순차적으로 하나씩
        for o in range(0,3):
            new_height = random.uniform(0.5, 2)  # 가로 세로 random 조정
            new_width = random.uniform(0.5, 2)
            new_height = round(new_height, 2)
            new_width = round(new_width, 2)
            for i in range(0, 2):  # png파일하나당 3개씩 만들기
                    add_number=0
                    new_seg = []
                    get_img = cv2.imread(file_path + '/' + str(j+add_number) + '.png')
                    resize_img = cv2.resize(get_img, dsize=(0, 0), fx=new_width, fy=new_height,
                                            interpolation=cv2.INTER_LINEAR)  # new_width가 갑자기 오류남 수정시작할것

                    for seg_len in range(0, len(json_data['annotations'][json_dic[str(j+add_number) + '.png']]['segmentation'][0][0])):
                        if seg_len % 2 == 0:  ##############################################################################################################
                            new_seg.append(json_data['annotations'][json_dic[str(j+add_number) + '.png']]['segmentation'][0][0][
                                               seg_len] * new_width)
                        else:
                            new_seg.append(
                                json_data['annotations'][json_dic[str(j+add_number) + '.png']]['segmentation'][0][0][
                                    seg_len] * new_height)
                    cv2.imwrite(file_path + '/' + str(files_amount + plus_number) + '.png', resize_img)
                    resize_img = cv2.imread(file_path + '/' + str(files_amount + plus_number) + '.png')
                    h, w = resize_img.shape[:2]
                    json_data['images'].append({  # json파일에서 image 부분 append
                        'id': img_amount+ files_amount + plus_number,
                        'dataset_id': 1,
                        'path': 'D:/wp/DW_intern/knife_data_file' + str(
                            img_amount+ files_amount + plus_number) + '.png',
                        'file_name': str(img_amount+files_amount + plus_number) + '.png',
                        'width': w,
                        'height': h})
                    json_data['annotations'].append({  # json파일에서 annotation 부분 append
                        'id': img_amount + files_amount + plus_number + 1,
                        'image_id': img_amount + files_amount + plus_number + 1,
                        'category_id': 1,
                        'bbox': [0, 0, w, h],
                        'segmentation': [[new_seg]],
                        'area': h * w,
                        'iscrowd': False,
                        'color': 'Unknown',
                        'unitID': 1,
                        'registNum': 1,
                        'number1': 4,
                        'number2': 4,
                        'weight': None})
                    add_number = add_number+1
                    plus_number += 1
    with open('json/'+str(file_path)+'.json', "w", encoding="UTF-8") as file:
        json.dump(json_data, file, indent=4)


def draw_ground_truth(file_path, json_data, json_dic, img_amount): # 본인 폴더, 본인 json, 본인 dic ,
    files_amount = files_count(file_path)
    for file_number in range(files_amount):
        img = cv2.imread(file_path + f"/{file_number}")
        img_copy = img.copy()
        bbox = []
        h, w = img.shape[:2]
        seg = json_data['annotations'][json_dic[str(file_number+img_amount) + '.png']]['segmentation'][0][0]
        result = []
        for i in range(0, len(json_data['annotations'][json_dic[str(file_number+img_amount) + '.png']]['segmentation'][0][0]),2):
            result.append(json_data['annotations'][json_dic[str(file_number+img_amount) + '.png']]['segmentation'][0][0][i:i + 2])
        vector = np.vectorize(np.int_)
        result = np.array(result)
        result = vector(result)
        # print(type(result))
        #print(result)
        for bbox_number in range(0, len(
                json_data['annotations'][json_dic[str(file_number) + '.png']]['bbox'])):
            bbox.append(json_data['annotations'][json_dic[str(file_number) + '.png']]['bbox'][bbox_number])
        img = cv2.fillPoly(img, [result], (0, 0, 255))
        img = cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 3)
        dst = cv2.addWeighted(img,0.2,img_copy,0.8,0)
        cv2.imwrite(file_path + str(file_number+img_amount) + '.png', dst)
        # cv2.imshow(f"{file_number}.png", dst)
        # cv2.waitKey()
        # cv2.destroyAllWindows()

#
if __name__ == '__main__':
    main()
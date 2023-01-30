import json
import cv2

data = {}
data['images'] = []
lista = ['high_1', 'low_1', 'high_2', 'low_2', 'high_3', 'low_3', 'high_4', 'low_4']
for i in range(0, 8):
    img = cv2.imread('background/' + lista[i] + '.png')
    print(img)
    h, w, _ = img.shape
    data['images'].append({
        'id': i,
        'path': 'D:/wp/DW_intern/background/' + (lista[i]),
        'file_name': lista[i],
        'width': w,
        'height': h, })
with open('json/background.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)


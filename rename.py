import os
import json
import cv2
from aug import files_count

def main():
    file_number=0
    image_number=0
    for folder_number in range(1,4):
        files_count(f"crop_artknife_{folder_number}")
        img = cv2.imread(f"crop_artknife_{folder_number}/{file_number}.png")
        cv2.imwrite('knife_data_file', f"{image_number}.png", img)
#
if __name__ == '__main__':
    main()



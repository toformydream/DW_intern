import os
import json
import cv2
from aug import files_count

def main():
    for i in range(0,20):
        img = cv2.imread('steak_knife/' + str(i) + '.png')
        cv2.imwrite('knife_data_file/' + str(i+104) + '.png', img)


if __name__ == '__main__':
    main()



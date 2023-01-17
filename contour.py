import cv2
import numpy as np
import matplotlib.pyplot as plt
def main():
    src = cv2.imread("knife_data_file/0.png", cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    binary = cv2.bitwise_not(binary)

    contours, hierachy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    keypoint = contours[0]
    epsilon1 = 0.04*cv2.arcLength(keypoint,True)
    appros1=cv2.approxPolyDP(keypoint, epsilon1, True)
    print("contours = ", contours)
    print(len(contours[0]))

    cv2.drawContours(src, [appros1], 0, (0, 0, 255), 2)
    cv2.imshow("src", src)
    cv2.waitKey(0)

    cv2.destroyAllWindows()












    # keypoints = []
    # img=cv2.imread("knife_data_file/0.png")
    # ret,binary = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
    # binary = cv2.bitwise_not(binary)
    # keypoints, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    # print(keypoints)
    # cv2.imshow('g', k)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
if __name__ == '__main__':
    main()

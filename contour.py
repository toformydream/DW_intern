import cv2
import numpy as np
def main():
    keypoints = []
    img=cv2.imread("knife_data_file/0.png")
    detector = cv2.xfeatures2d.SIFT_create()
    k = detector.detectAndCompute(img,None)
    print(k)
    # cv2.imshow('g', k)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
if __name__ == '__main__':
    main()

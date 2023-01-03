import cv2
import random
import numpy as np
#85가 마지막

high_img=cv2.imread("venv/crop_art_knife_2/84.png")
low_img=cv2.imread("venv/crop_art_knife_2/85.png")
random_number_width=random.randrange(100,1000)
random_number_height=random.randrange(100,1000)
resize_high_img = cv2.resize(high_img,(random_number_width,random_number_height))
resize_low_img = cv2.resize(low_img,(random_number_width,random_number_height))
print("resize_img.shape = {0}".format(resize_high_img.shape))
print("resize_img.shape = {0}".format(resize_low_img.shape))
cv2.imwrite('venv/crop_art_knife_2/338.png',resize_high_img)
cv2.imwrite('venv/crop_art_knife_2/339.png',resize_low_img)
random_number_width=random.randrange(100,1000)
random_number_height=random.randrange(100,1000)
resize_high_img = cv2.resize(high_img,(random_number_width,random_number_height))
resize_low_img = cv2.resize(low_img,(random_number_width,random_number_height))
print("resize_img.shape = {0}".format(resize_high_img.shape))
print("resize_img.shape = {0}".format(resize_low_img.shape))
cv2.imwrite('venv/crop_art_knife_2/340.png',resize_high_img)
cv2.imwrite('venv/crop_art_knife_2/341.png',resize_low_img)
random_number_width=random.randrange(100,1000)
random_number_height=random.randrange(100,1000)
resize_high_img = cv2.resize(high_img,(random_number_width,random_number_height))
resize_low_img = cv2.resize(low_img,(random_number_width,random_number_height))
print("resize_img.shape = {0}".format(resize_high_img.shape))
print("resize_img.shape = {0}".format(resize_low_img.shape))
cv2.imwrite('venv/crop_art_knife_2/342.png',resize_high_img)
cv2.imwrite('venv/crop_art_knife_2/343.png',resize_low_img)

#cv2.imshow("low",resize_low_img)
#cv2.imshow("high",resize_high_img)
cv2.waitKey()






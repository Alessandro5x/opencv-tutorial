import numpy as np
import cv2
import random

img = cv2.imread('assets/logo.jpg', -1)
#blue, green, red
#[255, 0, 0]
#for i in range(100): randow colors in a part of this image
#    for j in range(img.shape[1]):
#        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

#How to copy and paste a slice of this image
tag = img[50:150, 200:300]
img[100:200, 150:250] = tag


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
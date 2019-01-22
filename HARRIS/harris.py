# -*- coding:utf-8 -*-
# Author : Mazhen
# Date: 2019/1/22
import cv2
import numpy as np

filename = "D:\\11.jpg"
img = cv2.imread("D:\\masterstu\\imageData\\img\\1.jpg")
gray = cv2.imread(filename, 0)
gray = np.float32(gray)

# 输入图像必须是float32，最后一个参数在0.04 到0.05 之间
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
img[dst > 0.005*dst.max()] = [0, 0, 255]
cv2.imshow('dst', img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()


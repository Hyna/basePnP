import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('tape3.png')
img_rgbBlur = cv2.medianBlur(img_rgb, 5)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


imgX = cv2.medianBlur(img_gray, 5)
img2 = imgX.copy()


template = cv2.imread('template.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img2,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgbBlur, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

cv2.imwrite('res2.png',img_rgbBlur)


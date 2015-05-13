import numpy as np
import cv2

image1 = cv2.imread('blank.png', 0)
image2 = cv2.imread('resistors.png', 0)
image3 = image1 - image2

image4 = cv2.medianBlur(image1, 5)
image5 = cv2.medianBlur(image2, 5)
image6 = image4 - image5
image7 = image5 - image4


cv2.imwrite('out2.png',image6)
cv2.imwrite('out3.png',image7)



image3[image3 >= 210]= 128
image3[image3 < 50] = 128
image3[image3 <> range(50, 210)] = 0
cv2.imwrite('out4.png', image3)

image8 = cv2.medianBlur(image3, 5)

cv2.imwrite('out5.png', image8)

import numpy as np
import cv2
from matplotlib import pyplot as plt
import pprint
import math
import pprint
# based on http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html

pixpermm = 25.51
lastx = 0
lasty = 0

for i in range(0,17):
	#print('i: '+str(i))


	img = cv2.imread(str(i)+'.png',0) # CCD image
	img3 = cv2.medianBlur(img, 5)
	img2 = img3[140:340, 240:440]
	cv2.imwrite('hyna.png',img2) # CCD image

	cimg = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)
	



	crossColor = (255,0,0)
	crossThickenss = 1
	minDist = 50

	circles2 = cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1,minDist, param1=50,param2=30,minRadius=5,maxRadius=50)
	circles2 = np.uint16(np.around(circles2))
	#for i in circles2[0,:]:
		#print(i[0])
		#print(i[1])
		#print('-')
	if i>0:
		diffx=circles2.item(0)-lastx
		diffy=circles2.item(1)-lasty
		print( str(round(diffx /pixpermm,3)) + ';' + str(round(diffy /pixpermm,3)))
		#print( )
	lastx = circles2.item(0)
	lasty = circles2.item(1)


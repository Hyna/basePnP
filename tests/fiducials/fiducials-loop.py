import numpy as np
import cv2
from matplotlib import pyplot as plt
import pprint
import math
import pprint
# based on http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html
from PyQt4 import QtCore, QtGui

import time
#img1 = cv2.imread('IC_template2.png',0) # template
#img = cv2.imread('/home/hyna/Diplomka/sw/basePnP/doc/mereni/fiducials/fiduc_svetlostrop_crop.png',0) # CCD image
crossColor = (255,0,0)
crossThickenss = 1

capture = cv2.VideoCapture(0)    

for x in range(0, 100):
	value, img = capture.read()

	cv2.imwrite( 'h.png', img)
	img =  cv2.imread( 'h.png', 0)


	img2 = cv2.medianBlur(img, 5)
#pprint.pprint(img) # check -  img is none fue to wrong path or type. eg. jpg.

#img2 = cv2.Canny(img,20,330)

	cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
	cimg2 = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)







	minDist = 150 # min distance between circles centers. Low enough value can even find circle inside circle. But it generates so many circles(useless). High value on the other side generate smaller amount of circles, but can miss the right one. So the strategy for PCB fiducials will be: Corp the CCD image only to small area where fiducial is expected. Use lower minDist value




	circles2 = cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1,minDist, param1=50,param2=30,minRadius=5,maxRadius=30)



	circles2 = np.uint16(np.around(circles2))
	for i in circles2[0,:]:
		# draw the outer circle
		cv2.circle( cimg2,(i[0],i[1]),i[2],(0,255,0),2)
		# draw the crosshair
		cv2.line(cimg2, (i[0]-25, i[1]), (i[0]+25, i[1]), crossColor,crossThickenss) # horizontal line
		cv2.line(cimg2, (i[0], i[1]-25), (i[0], i[1]+25), crossColor,crossThickenss) # vertical line

	pprint.pprint(circles2)
	time.sleep(1)


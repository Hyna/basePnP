import numpy as np
import cv2
from matplotlib import pyplot as plt
import pprint
import math
import pprint



class FiducialFinder:
	'fiducial finder, take an argument with fiducial size. getPosition take image parameter and return center position of fiducial. Throws an error if <> 1 fiducials are found. Only CORPED color input image is expected to eliminate >1 fiducial.'

	def __init__(self, fiducialSize):
		self.fiducialSize = fiducialSize
		self.minDist = 150
		''' min distance between circles centers. Low enough value can even find circle inside circle. But it generates so many circles(useless).
		    High value on the other side generate smaller amount of circles, but can miss the right one.
		    So the strategy for PCB fiducials will be: Corp the CCD image only to small area where fiducial is expected. Use lower minDist value.
		'''

	def getPosition(self, img):
		grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		blurImg = cv2.medianBlur(grayImg, 5) # image is blured, it gives beter precision. See tests/fiducials/fiducials.py
		circles = cv2.HoughCircles(blurImg,cv2.HOUGH_GRADIENT,1,self.minDist,
                            param1=50,param2=30,minRadius=10,maxRadius=45)
		circles = np.uint16(np.around(circles))
		circlesCount = circles[0].shape[0]
		#pprint.pprint(circlesCount)
		if circlesCount > 1:
			raise ValueError('More than one fiducial was found!')
		if circlesCount < 1:
			raise ValueError('No fiducial was found!')
		
		print 'Fiducial found.'
		return circles[0][0]


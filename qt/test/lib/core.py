import numpy as np
import pprint
import math
import cv2
from PyQt4 import QtCore, QtGui

# documentation: none

# tests: No tests at all


class Core:
	'setup'

	def __init__(self, mainWindow):
		self.mainWindow = mainWindow


		self.version = '0.2 alpha'

		# TODO Load these values from file
		self.topPixelPermm = 25.51 # top camer pixel per mm
		self.bottomPixelPermm = 666 #bottom camera pixel per mm
		self.topCCDHeight = 480
		self.topCCDWidth = 640

		#self.boardOffset = [6,245] # X,Y position where 0,0 of board is. Board workplace; => transefered to Board module
		

	def toPix(self, mm, camera):
		#TODO - make a input values check
		#	raise ValueError('toPx function does not accept 0  as input value!')
		if camera == 0:		
			pix = mm*self.topPixelPermm
		else:
			pix = mm*self.bottomPixelPermm
		return pix


	def tomm(self, pix, camera):
		#TODO - make a input values check
		#	raise ValueError('tomm function does not accept 0  as input value!')
		if camera == 0:		
			mm = pix/self.topPixelPermm
		else:
			mm = pix/self.bottomPixelPermm
		return mm
	
	def getVersion(self):
		return self.version

	def getTestImage(self):
		pixmap = QtGui.QPixmap('fiducial3.png')
		return pixmap

	def getTopImage(self):
		camcapture = cv2.VideoCapture(0)       
		ret, frame = camcapture.read()

		image4 = QtGui.QImage(frame,640,480, QtGui.QImage.Format_RGB888).rgbSwapped()
		pixmap = QtGui.QPixmap.fromImage(image4)
		return pixmap	
		#label.setPixmap(pixmap)

	def log(self, wat):
		self.mainWindow.listTerminal.addItem(str(wat))
		self.mainWindow.listTerminal.scrollToBottom()



'''
core = Core()
version = core.getVersion()
pprint.pprint(version)

test = core.toPix(4, 0)
pprint.pprint(test)

test2 = core.tomm(10, 0)
pprint.pprint(test2)
'''

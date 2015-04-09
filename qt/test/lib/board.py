import pprint as pp
import numpy as np

import core as libCore
import machine as libMachine

from PyQt4 import QtCore, QtGui
import cv2
from qimage2ndarray import rgb_view
import time
from lib import transform as tr


class Board:
	'board alignmentm'


	def __init__(self, mainWindow):
		self.mainWindow = mainWindow
		self.aligned = False
		self.mode = 1 # mode 1 means Manual Zero position - no fiducials

		self.boardOffset = [7.801,143.6]
		#self.fiducials = libFiducials.fiducialFinder()

		self.hasFiducials = False
		self.fiducialsCount = 0
		self.fiducials = []
		self.fiducialsFound = []

		# TODO Load these variables from file
		self.fiducialSize = 1.0 # float diameter in mm


	def setBoardOffset(self, offset):
		self.boardOffset = offset
		pp.pprint('Board.setboardOffset(): New board offset was set.')


	def mode1(self):
		#machine = libMachine.Machine()
		pos = self.mainWindow.machine.currentPos()
		#pprint.pprint(pos)
		self.setBoardOffset(pos)

		self.aligned = True
		self.mainWindow.lblBoardStatus.setText('Board is aligned in MODE1.')



	def mode3(self):
		if self.fiducialsCount != 3:
			pp.pprint('Wrong count of fiducials. 3 expected and '+str(self.fiducialsCount)+' given')
		else:
			# get the fiducail size in px
			pixFiducSize = self.mainWindow.core.toPix( self.fiducialSize, 0)
			pp.pprint('Size of Fiducial in pix'+str(pixFiducSize))
			# add 50% to real fiducial size to eliminate possible misalignment
			# TODO fix hack -30

			cropSize = pixFiducSize*3 # only one axis since crop area is square

			CCDWidth = self.mainWindow.core.topCCDWidth
			CCDHeight = self.mainWindow.core.topCCDHeight

			cropCenter = [CCDWidth/2-cropSize/2, CCDHeight/2-cropSize/2 ]
			rect = QtCore.QRect(cropCenter[0],cropCenter[1], cropSize, cropSize)


			self.mainWindow.imgFiduc1.setScaledContents(True) 
			self.mainWindow.imgFiduc2.setScaledContents(True) 
			self.mainWindow.imgFiduc3.setScaledContents(True) 

			#for fiducial in self.fiducials:
			for i in [0,1,2]:
				pp.pprint('Fiducial ' + str(i) + ' X:'+ str(self.fiducials[i][0])+ 'Y:'+ str(self.fiducials[i][1]) )

				pos = self.transform(self.fiducials[i]) # only basic transformation in mode 1
				pp.pprint('was transformed to X:'+ str(pos[0])+ 'Y:'+ str(pos[1]) )				

				self.mainWindow.machine.goTo(pos, 1500)
				
				time.sleep(4)
				pixmap = self.mainWindow.core.getTopImage()
				time.sleep(2)
				croppedImg = pixmap.copy(rect)
				#pp.pprint(cropped)
				if i == 0:				
					self.mainWindow.imgFiduc1.setPixmap(croppedImg)
				if i == 1:				
					self.mainWindow.imgFiduc2.setPixmap(croppedImg)
				if i == 2:				
					self.mainWindow.imgFiduc3.setPixmap(croppedImg)

				# http://hmeine.github.io/qimage2ndarray/#converting-qimages-into-numpy-ndarrays
				try:			
					posFound = self.getFiducPos(rgb_view(croppedImg.toImage()))
					pp.pprint(posFound)
					pp.pprint('Fiducial '+ str(i)+' found at pix X: '+str(posFound[0])+ ' Y:'+ str(posFound[1]))
				except ValueError:
					pp.pprint('fiducial '+ str(i)+' not found')
					self.mainWindow.lblBoardStatus.setText('Failed to align - fiducial '+ str(i)+' not found.')
					return


				todo = rect.getRect()
				pp.pprint('width ' +str(todo[2]))
				pp.pprint('height '+str(todo[3]))
				x = (todo[2]/2 - posFound[0])
				y = (todo[3]/2 - posFound[1])*-1

				posError = [self.mainWindow.core.tomm(x, 0), self.mainWindow.core.tomm(y, 0)]
				pp.pprint('Positioning error in mm X: '+str(posError[0])+ ' Y:'+ str(posError[1]))
	
				paint = QtGui.QPainter(croppedImg);
				pen = QtGui.QPen(QtGui.QColor(255,255,0,255), 1)
				paint.setPen(pen)
				paint.drawLine(posFound[0], posFound[1]-30, posFound[0], posFound[1]+30   );
				paint.drawLine(posFound[0]-30, posFound[1], posFound[0]+30, posFound[1]   );
				del paint # important!

				if i == 0:				
					self.mainWindow.imgFiduc1.setPixmap(croppedImg)
				if i == 1:				
					self.mainWindow.imgFiduc2.setPixmap(croppedImg)
				if i == 2:				
					self.mainWindow.imgFiduc3.setPixmap(croppedImg)

				realPos = [round(pos[0]-posError[0],3),round(pos[1]-posError[1],3)]
				#realPos = [pos[0],pos[1]]
				self.fiducialsFound.append(realPos)
				#self.mainWindow.imgFiduc1.setPixmap(croppedImg)
				
			pp.pprint(self.fiducialsFound)
			self.aligned = True	
			self.mode = 3
			self.mainWindow.lblBoardStatus.setText('Board is aligned in MODE3.')
		

	def clear(self):
		self.aligned = False
		self.mode = 1
		self.fiducialsFound = []
		self.mainWindow.lblBoardStatus.setText('Board is NOT aligned.')

	def transform(self, pos):
		if self.mode == 1:

			xnew = self.boardOffset[0] + pos[0]
			ynew = self.boardOffset[1] + pos[1]
			newpos = [xnew , ynew]
			return newpos
		elif self.mode == 3:


			#from_pt = ((1,1),(4,1),(4,4)) # a 1x1 rectangle
			#to_pt = ((4,1),(7,1),(7,4))   # scaled x 2, rotated 45 degrees and translated

			from_pt = (self.fiducials)
			to_pt = (self.fiducialsFound[0],self.fiducialsFound[1],self.fiducialsFound[2])
			pp.pprint('-----------')			
			pp.pprint(self.fiducials)
			pp.pprint(self.fiducialsFound)
			pp.pprint('-----------')

			#http://elonen.iki.fi/code/misc-notes/affine-fit/
			self.trn = tr.Affine_Fit(from_pt, to_pt)

			print "Transformation is:"
			print self.trn.To_Str()
			

			return self.trn.Transform((float(pos[0]), float(pos[1])))

		else:
			return value
	def addFiducial(self, pos):
		self.fiducials.append(pos)
		self.hasFiducials = True
		self.fiducialsCount =  self.fiducialsCount + 1

	def getFiducPos(self, img):
		minDist = 150

		grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		blurImg = cv2.medianBlur(grayImg, 5) # image is blured, it gives beter precision. See tests/fiducials/fiducials.py
		circles = cv2.HoughCircles(blurImg,cv2.HOUGH_GRADIENT,1,minDist,
                            param1=50,param2=30,minRadius=10,maxRadius=45)
		#pp.pprint(circles)
		if circles is None:
			raise ValueError('No fiducial was found!')

		circles = np.uint16(np.around(circles))

		circlesCount = circles[0].shape[0]
		#pprint.pprint(circlesCount)
		if circlesCount > 1:
			raise ValueError('More than one fiducial was found!')

		
		print 'Fiducial found.'
		return circles[0][0]
	

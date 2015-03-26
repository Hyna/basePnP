#!/usr/bin/env python

import sys
import os
from PyQt4 import QtCore, QtGui, uic
from test import Ui_MainWindow
import pprint #for debug - pprint.pprint(variable) dumps a variables
import numpy as np
import cv2
import qimage2ndarray as i2a

import transform as tr

import time

from lib import core as libCore
from lib import machine as libMachine
from lib import board as libBoard
from lib import devices as libDevices


from tabs.motion import *

class StartQT4(QtGui.QMainWindow):
	def __init__(self, *args):
		super(StartQT4, self).__init__(*args)
		
		ui = uic.loadUi('mainwindow.ui', self)
		#all code must be inserted after self.ui.setupUi(self)

		

		self.imgCCD.mousePressEvent = self.doSomething
		self.align = False
		self.alignState = ''


 		# core initialization - basic functions and setup
		self.core = libCore.Core(ui)
		pprint.pprint(self.core.getVersion())

		# load machine module - connection to the machine will be done later
		self.machine = libMachine.Machine()

		# board alignment and coordinates transformation
		#ui =  Ui_MainWindow()
		self.board = libBoard.Board(ui)


 		# Devices initialization
		self.devices = libDevices.Devices(ui)


		self.treeWidget.itemDoubleClicked.connect(self.what)
		#self.treeDevices.itemDoubleClicked.connect(self.devices)

	@QtCore.pyqtSlot(QtGui.QTreeWidgetItem)
	def what(self, item):
		# dojede na dane misto po dvojkliku na soucastku
		pprint.pprint('yeah'+str(item))
		pprint.pprint(item.text(4))
		pprint.pprint(item.text(5))
		xy = [float(item.text(4)),float(item.text(5))]
		pprint.pprint(xy)
		transform = self.board.transform(xy)
		pprint.pprint(transform)
		self.machine.addToQueue('G0 X'+str(transform[0])+' Y'+str(transform[1])+ ' F 2000')
		self.machine.dumpQueue()
		self.machine.run()
		time.sleep(0.3)
		self.on_btnLoadCCD_clicked()




	def doSomething(self, event):
		#pprint.pprint('ABC')	
		#pprint.pprint(event.x())	
		#pprint.pprint(event.y())
		if self.align == True:

			pos = []

			label =self.imgCCD
			#a = label.size()
			#y = a.height()-event.y()
			pos.append(event.x())
			pos.append(event.y())
			#pos.append(y ) # eagle has 00 at left bottom corner but Qlabel has 00 at top left corner

			

			img = QtGui.QImage(self.imgCCD.pixmap())
			img.convertToFormat(QtGui.QImage.Format_ARGB32)

			#image = self.convertQImageToMat(img)
			pprint.pprint(img.width())
			#
			
			nparray = i2a.rgb_view(img)

			nparray2 = cv2.cvtColor(nparray, cv2.COLOR_BGR2RGB) #

			#image = cv2.imread(nparray)
			
			#QtGui.QImage.Format_RGB888
			cv2.imwrite('test.png', nparray2);
			#cv2.imwrite('test.png', nparray.rgbSwapped());
			


			if self.alignState == 'p3':
				self.p3 = pos
				pprint.pprint('Fiducial p3 is aligned')
				self.lblP3.setText('X:'+str(self.p3[0])+' Y:'+str(self.p3[1]))
				#self.ui.btnLoadCCD.setText('aaaaaaaaaa')

		
			if self.alignState == 'p2':
				self.p2 = pos
				pprint.pprint('Fiducial p2 is aligned')
				self.lblP2.setText('X:'+str(self.p2[0])+' Y:'+str(self.p2[1]))
				self.alignState = 'p3'

			if self.alignState == 'p1':
				self.p1 = pos
				self.alignState = 'p2'
				pprint.pprint('Fiducial p1 is aligned')
				self.lblP1.setText('X:'+str(self.p1[0])+' Y:'+str(self.p1[1]))





	@QtCore.pyqtSlot()
	def on_btnBoardM1_clicked(self):


		self.board.mode1()

		
	@QtCore.pyqtSlot()
	def on_btnBoardM3_clicked(self):
		#pos = self.machine.currentPos()
		#pprint.pprint(pos)

		#self.board.setBoardOffset(pos)
		self.board.mode3()


		'''
		#self.btnCenter.setText(str(self.core.boardOffset[0]) )
		gcode = 'G0 X'+str(self.core.boardOffset[0]) + ' Y'+ str(self.core.boardOffset[1])+ ' F4000' 
		#self.machine.addToQueue('G91')
		self.machine.addToQueue(gcode)
		self.machine.addToQueue('G90')
		self.machine.dumpQueue()
		self.machine.run()
		'''
	@QtCore.pyqtSlot()
	def on_btnClearAlignment_clicked(self):
		self.board.clear()



	@QtCore.pyqtSlot()
	def on_btnCenter_clicked(self):
		#self.btnCenter.setText(str(self.core.boardOffset[0]) )
		self.machine.goTo(self.board.boardOffset, 4000 )



	@QtCore.pyqtSlot()
	def on_btnHome_clicked(self):
		self.machine.home()

	@QtCore.pyqtSlot()
	def on_btnMoveXn_clicked(self):
		self.machine.relMove('X', -1, 2000)
		'''
		gcode = 'G0 X-1 F2000' 
		self.machine.addToQueue('G91')
		self.machine.addToQueue(gcode)
		self.machine.addToQueue('G90')
		self.machine.dumpQueue()
		self.machine.run()
		'''
	@QtCore.pyqtSlot()
	def on_btnMoveXn1_clicked(self):
		self.machine.relMove('X', -0.1, 2000)

	@QtCore.pyqtSlot()
	def on_btnMoveXn2_clicked(self):
		self.machine.relMove('X', -10, 2000)


	@QtCore.pyqtSlot()
	def on_btnMoveXp_clicked(self):
		self.machine.relMove('X', 1, 2000)		

	@QtCore.pyqtSlot()
	def on_btnMoveXp1_clicked(self):
		self.machine.relMove('X', 0.1, 2000)

	@QtCore.pyqtSlot()
	def on_btnMoveXp2_clicked(self):
		self.machine.relMove('X', 10, 2000)


	@QtCore.pyqtSlot()
	def on_btnMoveYn_clicked(self):
		self.machine.relMove('Y', -1, 2000)

	@QtCore.pyqtSlot()
	def on_btnMoveYn1_clicked(self):
		self.machine.relMove('Y', -0.1, 2000)

	@QtCore.pyqtSlot()
	def on_btnMoveYn2_clicked(self):
		self.machine.relMove('Y', -10, 2000)


	@QtCore.pyqtSlot()
	def on_btnMoveYp_clicked(self):
		self.machine.relMove('Y', 1, 2000)

	@QtCore.pyqtSlot()
	def on_btnMoveYp1_clicked(self):
		self.machine.relMove('Y', 0.1, 2000)

	@QtCore.pyqtSlot()
	def on_btnMoveYp2_clicked(self):
		self.machine.relMove('Y', 10, 2000)


	#mega decorators :)
	@QtCore.pyqtSlot()
	def on_imgCCD_mousePressEvent(self):
		pprint.pprint('EZFGFSG')


	@QtCore.pyqtSlot()
	def on_btnConnect_clicked(self):
		if self.machine.isConnected() is True:
			pass
			self.machine.disconnect()
			self.lblMachineStatus.setText('Machine was disconnected')
			self.btnConnect.setText('Connect')
		else:
			port = self.txtPort.text()	
			if self.machine.connect('/dev/ttyACM0'):
				self.lblMachineStatus.setText('Machine was connected')
				self.btnConnect.setText('Disconnect')

			else:
				self.lblMachineStatus.setText('Unable to connect!')
			#pprint.pprint(self.txtPort.text())
			#self.btnConnect.setText('Connect')
		

	@QtCore.pyqtSlot()
	def on_btnAlign_clicked(self):
		if self.align == False:
			self.align = True
			self.alignState = 'p1' # initial state

			#self.lblO1.setText(self.fiduc[0][0])
			self.lblO1.setText('X:'+str(self.fiduc[0][0])+' Y:'+str(self.fiduc[0][1]))
			self.lblO2.setText('X:'+str(self.fiduc[1][0])+' Y:'+str(self.fiduc[1][1]))
			self.lblO3.setText('X:'+str(self.fiduc[2][0])+' Y:'+str(self.fiduc[2][1]))
			print('self align True')
		else:
			#points are aligned so we can make coordinates transformation
			self.align = False


			#from_pt = ((1,1),(4,1),(4,4)) # a 1x1 rectangle
			#to_pt = ((4,1),(7,1),(7,4))   # scaled x 2, rotated 45 degrees and translated

			from_pt = (self.fiduc)
			to_pt = (self.p1,self.p2,self.p3)
			#pprint.pprint(self.p1)
			#pprint.pprint(self.fiduc)

			#http://elonen.iki.fi/code/misc-notes/affine-fit/
			trn = tr.Affine_Fit(from_pt, to_pt)

			print "Transformation is:"
			print trn.To_Str()
			
			label =self.imgCCD
			label.setScaledContents(True) 
			pixmap = QtGui.QPixmap('base3D_mk3_012.mnt.png')

			a = label.size()
			b = pixmap.size()
			pprint.pprint(a)
			pprint.pprint(b)
			ratioW =float(b.width())/float(a.width())
			ratioH =float(b.height())/float(a.height())
			# TODO mozno predelat na 
			# QPixmap scaledToHeight
			# QPixmap scaledToWidth
			pprint.pprint(ratioW)
			
			#http://stackoverflow.com/questions/17888795/how-to-use-qpainter-on-qpixmap
			paint = QtGui.QPainter(pixmap);
			pen = QtGui.QPen(QtGui.QColor(255,255,0,255), 4)
			paint.setPen(pen)

			#
			for origin in self.origins:
				#paint.drawRect(5,5,float(origin[1])*25,float(origin[2])*25);
				tOrigin =  trn.Transform((float(origin[3]),float(origin[4])))
				tOrigin[0] = tOrigin[0]*ratioW # kompenzace scaledContent
				tOrigin[1] = tOrigin[1]*ratioH #
				paint.drawLine(tOrigin[0]-10, tOrigin[1], tOrigin[0]+10, tOrigin[1]   );
				paint.drawLine(tOrigin[0], tOrigin[1]-10, tOrigin[0], tOrigin[1]+10   );
				#pprint.pprint(origin[2])


			#paint.drawRect(15,15,100,100);
			del paint
			label.setPixmap(pixmap)
			print('self align False')






	@QtCore.pyqtSlot()
	def on_btnLoadTst_clicked(self):

 		label =self.imgCCD
		label.setScaledContents(True) 
		
		
		pixmap = QtGui.QPixmap('base3D_mk2.mnt.png')
		label.setPixmap(pixmap)



	#mega decorators :)
	@QtCore.pyqtSlot()
	def on_btnLoadCCD_clicked(self):
		label =self.imgCCD2
		#label = self.labelka	

		#label.setFixedSize(500,300)
		#label.move(480, 190)

		#label.setScaledContents(True) 
		#pixmap = QtGui.QPixmap('base3D_mk3_012.mnt.png')
		#label.setPixmap(pixmap)
		

		#img = cv2.imread('base3D_mk3_012.mnt.png',0) # template
		#img2 = cv2.resize(img, (100,200))

		
		# TODO  udelat online stream podle http://paste.fedoraproject.org/202220/42721993/
		camcapture = cv2.VideoCapture(0)       
		#camcapture.set(CV_CAP_PROP_FRAME_WIDTH, 1280)
		#camcapture.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 720);

		ret, frame = camcapture.read()

		image4 = QtGui.QImage(frame,640,480, QtGui.QImage.Format_RGB888).rgbSwapped()
		pixmap = QtGui.QPixmap.fromImage(image4)


		paint = QtGui.QPainter(pixmap);
		pen = QtGui.QPen(QtGui.QColor(255,0,0,255), 1)
		paint.setPen(pen)
		paint.drawLine(0, 240, 640, 240   );
		paint.drawLine(320, 0, 320, 480   );
		del paint # important!


		label.setPixmap(pixmap)
		


	@QtCore.pyqtSlot()
	def on_btnLoadPlacement_clicked(self):
		
		#fd = QtGui.QFileDialog(self)
		#self.filename = fd.getOpenFileName()

		#for debug purposes only
		self.filename = 'base3D_mk2.mnt'
			
		from os.path import isfile
		if isfile(self.filename):
			data = 0
			fiducials = 0
			with open(self.filename, 'r') as fo:
				array = [] # array of lines. not yet exploded.
				array_split = [] # two dimensional array with exploded lines
				self.fiduc = []
				for line in fo:
					if line.startswith('%end_data'):
						data = 0
					if data == 1:
						# remove \n from end of the line and append to the list
						strip_line = line.rstrip()						
						array.append(strip_line)

						pole = []
						values = strip_line.split(';')						
						for value in values:
							pole.append(value)
							#pprint.pprint(value)
						array_split.append(pole)

					if line.startswith('%data'):
						data = 1

					if line.startswith('%end_fiducials'):
						fiducials = 0
					if fiducials == 1:
						strip_line = line.rstrip()
						values2 = strip_line.split(';')	

						fiducial = []
						fiducial.append(float(values2[3])) # Xorigin
						fiducial.append(float(values2[4])) # Yorigin
						self.fiduc.append(fiducial)	
					
						#ok ////
						self.board.addFiducial(fiducial)					

					if line.startswith('%fiducials'):

						fiducials = 1
			pprint.pprint(self.fiduc)
			
			# OK ////
			self.lblO1.setText('X:'+str(self.board.fiducials[0][0])+' Y:'+str(self.board.fiducials[0][1]))
			self.lblO2.setText('X:'+str(self.board.fiducials[1][0])+' Y:'+str(self.board.fiducials[1][1]))
			self.lblO3.setText('X:'+str(self.board.fiducials[2][0])+' Y:'+str(self.board.fiducials[2][1]))

			# setting header labels
			tree = self.treeWidget
			tree.setHeaderLabels(['Part name','Package','Value', 'Rotation','X origin','Y origin', 'X center','Y center'])
			tree.setColumnWidth(0, 70)
			tree.setColumnWidth(1, 70)
			tree.setColumnWidth(2, 70)
			tree.setColumnWidth(3, 70)
			tree.setColumnWidth(4, 70)
			tree.setColumnWidth(5, 70)
			tree.setColumnWidth(6, 70)
			tree.setColumnWidth(7, 70)
			tree.setColumnCount(8)

			# setting header labels
			tree2 = self.treePackages
			tree2.setHeaderLabels(['Device|value','Place','Tray'])
			tree2.setColumnCount(3)
			tree2.setColumnWidth(0, 150)
			tree2.setColumnWidth(1, 70)
			tree2.setColumnWidth(2, 70)

			

			array2 = array # copy of array with lines
			dic = {}
			self.origins = array_split
			
			
			
			# Defines recursive dictionary TEST only
			#tree=lambda: defaultdict(tree)

			for item in array2:
				items = item.split(';')
				

				#pprint.pprint(items[7])
				index = items[7]+'|'+items[6]
				
				
				

				if index in dic:
					#pprint.pprint('ok')
					
					dic2 = dic[index]					
					count = len(dic2)
					dic2[count] = items

					
										
				else:
					#pprint.pprint('Nok pridavam')
					

					dic2 = {}

					dic2[0] = items
					#dic2 = dic[index]
					
					#pprint.pprint(count)
					#dic[index] = items
					dic[index] = dic2

			#pprint.pprint(dic)


			# Display list of all devices exported from eagle
			for item in array:
				row = QtGui.QTreeWidgetItem(self.treeWidget)

				# split the line into separate variables
				items = item.split(';')
	
				row.setText(0, items[0]) # Part name
				row.setText(1, items[7]) # package
				row.setText(2, items[6]) # value
				row.setText(3, items[5]) # rotation
				row.setText(4, items[3]) # X origin
				row.setText(5, items[4]) # Y origin
				row.setText(6, items[1]) # X pads center
				row.setText(7, items[2]) # Y pads center
				

			# display groups of devices with same PACKAGE/VALUE
			for key, item in dic.items():
				#pprint.pprint('jsem tu')				
				row = QtGui.QTreeWidgetItem(self.treePackages)
				row.setText(0, key) # Group package|value
				row.setText(2, 'tray: None') # tray
				row.setCheckState(1, QtCore.Qt.Checked)

				for key2, item2 in dic[key].items():
					subrow = QtGui.QTreeWidgetItem(row)
					#pprint.pprint(item2)				
					subrow.setText(0, item2[0]) # Part name|value
										
					subrow.setCheckState(1, QtCore.Qt.Checked)
					#subrow.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)

					self.combo = QtGui.QComboBox()
					

	@QtCore.pyqtSlot()
	def on_btnAddDevice_clicked(self):
		self.devices.add()


	@QtCore.pyqtSlot()
	def on_btnEditDevice_clicked(self):
		self.devices.edit()

	@QtCore.pyqtSlot()
	def on_btnRemoveDevice_clicked(self):
		self.devices.removeDevice()

	@QtCore.pyqtSlot()
	def on_btnStSave_clicked(self):
		self.devices.saveDevice()

	@QtCore.pyqtSlot()
	def on_btnStAlign_clicked(self):
		#testovaci hack
		self.devices.getPickPos(self.txtDeviceName.text())


class MyLabel(QtGui.QLabel):
    """A Label widget derived from QTextEdit and implementing its
       own paintEvent"""

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawLine(0, 10, 10, 10)
        QtGui.QLabel.paintEvent(self, event)
	




if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartQT4()
	myapp.show()
	sys.exit(app.exec_())

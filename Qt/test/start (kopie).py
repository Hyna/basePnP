import sys
import os
from PyQt4 import QtCore, QtGui
from test import Ui_MainWindow
import pprint #for debug - pprint.pprint(variable) dumps a variables
import numpy as np




import transform

class StartQT4(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self._labelka = MyLabel(self)
		#QtGui.QMainWindow.addWidget(self.labelka, 0, 0)

		#lbl1 = MyLabel(self)
		#lbl1.move(15, 10)
		
		#all code must be inserted after self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.btnLoadPlacement,QtCore.SIGNAL("clicked()"), self.file_dialog)
		QtCore.QObject.connect(self.ui.btnLoadCCD,QtCore.SIGNAL("clicked()"), self.load_test)
		#QtCore.QObject.connect(self.ui.btnLoadTst,QtCore.SIGNAL("clicked()"), self.draw_test)

	#def paintEvent(self, event):
		#painter = QtGui.QPainter(self.ui.btnLoadTst)
		#painter.begin(self.ui.imgCCD)
		#painter.setBrush(QtGui.QBrush(QtCore.Qt.red))
		#painter.drawEllipse(0, 0, self.width() - 1, self.height() - 1)
		#painter.end()




	def load_test(self):
		#label =self.ui.imgCCD
		label =self.ui.labelka	
		label.setScaledContents(True) 
		label.setPixmap(QtGui.QPixmap('base3D_mk3_012.mnt.png'))

	def file_dialog(self):
		#self.ui.btnLoadCCD.setText('aaaaaaaaaa')
		
		#fd = QtGui.QFileDialog(self)
		#self.filename = fd.getOpenFileName()

		#for debug purposes only
		self.filename = '/home/hyna/Diplomka/sw/Qt/test/base3D_mk3_012.mnt'
		
		from os.path import isfile
		if isfile(self.filename):
			
			data = 0
			

			with open(self.filename, 'r') as fo:
				array = []
				for line in fo:

					if line.startswith('%end_data'):
						data = 0

					if data == 1:
						# remove \n from end of the line and append to the list
						array.append(line.rstrip())
	
					if line.startswith('%data'):
						data = 1

			# setting header labels
			tree = self.ui.treeWidget
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
			tree2 = self.ui.treePackages
			tree2.setHeaderLabels(['Device|value','Place','Tray'])
			tree2.setColumnCount(3)
			tree2.setColumnWidth(0, 150)
			tree2.setColumnWidth(1, 70)
			tree2.setColumnWidth(2, 70)


			array2 = array
			dic = {}
			
			
			# Defines recursive dictionary TEST only
			tree=lambda: defaultdict(tree)

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

			pprint.pprint(dic)


			for item in array:
				row = QtGui.QTreeWidgetItem(self.ui.treeWidget)

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
				


			for key, item in dic.items():
				pprint.pprint('jsem tu')				
				row = QtGui.QTreeWidgetItem(self.ui.treePackages)
				row.setText(0, key) # Group package|value
				for key2, item2 in dic[key].items():
					subrow = QtGui.QTreeWidgetItem(row)
					pprint.pprint(item2)				
					subrow.setText(0, item2[0]) # Part name|value
					
					subrow.setText(1, '.') #place					
					subrow.setCheckState(1, QtCore.Qt.Checked)
					#subrow.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)

					self.combo = QtGui.QComboBox()
					

					subrow.setText(2, 'tray ???') # tray


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

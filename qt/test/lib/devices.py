from PyQt4 import QtCore, QtGui
import pprint as pp
import time


class Devices:
	'holds the information about devices'


	def __init__(self, mainWindow):
		self.mainWindow = mainWindow
		self.devices = {}


	def add(self):

		name = self.mainWindow.txtDeviceName.text()
		if name == '':
			self.mainWindow.core.log('info: Part was not created - Insert the name')
			return
		else:
			self.mainWindow.core.log('New device name is: ' +name)
			self.mainWindow.txtDeviceName.setText('')

		ftype = self.mainWindow.boxFeederType.currentText()
		status = 0
		# status 0: Not aligned;
		# status 1: Empty;
		# status 2: Valid;
		properties = []
		device = [ str(ftype), status, properties]
		#self.devices.append(device)

		self.devices[name] = device
		self.show()

	def getDevices(self):
		return self.devices

	def show(self):
		status = ['Not aligned','Empty','Valid']
		self.mainWindow.treeDevices.clear()
		for index, device in self.devices.items():
		#for key, value in mydic.items()

			row = QtGui.QTreeWidgetItem()
			row.setText(0, index) # name
			row.setText(1, device[0]) # feeder type

			row.setText(2, status[device[1]]) # status
			self.mainWindow.treeDevices.addTopLevelItem(row)

	def edit(self):
		#pp.pprint(self.mainWindow.treeDevices.selectedItems())
		selectedDev = self.mainWindow.treeDevices.selectedItems()

		if selectedDev == []:
			self.mainWindow.core.log('No device selected for edit')
			return
		
		devIndex = selectedDev[0].text(0)
		device = self.devices[devIndex]
		pp.pprint(device)

		self.mainWindow.txtDeviceName.setText(devIndex)
		
		if device[2] != []:
			pp.pprint('lolzz')

	def removeDevice(self):
		selectedDev = self.mainWindow.treeDevices.selectedItems()

		if selectedDev == []:
			self.mainWindow.core.log('No device selected for deleting')
			return
		
		devIndex = selectedDev[0].text(0)
		del self.devices[devIndex]
		self.mainWindow.core.log('Device was deleted')
		self.show()


	def saveDevice(self):
		name = self.mainWindow.txtDeviceName.text()
		if name == '':
			self.mainWindow.core.log('info: Part was not saved - Name is missing')
			return

		pitch = self.mainWindow.txtStPitch.text()
		if pitch == '':
			self.mainWindow.core.log('info: Pitch was not set')
			return

		partCount = self.mainWindow.boxStCount.value()
		currentIndex = self.mainWindow.boxStIndex.value()

		if currentIndex > partCount:
			self.mainWindow.core.log('info: Current index cant be higher than part count')
			return

		properties = []
		properties.append(int(pitch)) #
		properties.append(partCount)
		properties.append(currentIndex)

		#TODO toto je jen hack, dodelat centrovani prvni pozice
		firstPos = self.mainWindow.machine.currentPos()
		properties.append(firstPos)
		currentPos = firstPos
		properties.append(currentPos)

		self.mainWindow.core.log('info: All correct. Can save')	
		self.devices[name][1] = 2 # set status as valid
		self.devices[name][2] = properties
		pp.pprint(self.devices[name])
		self.show()



	def getPickPos(self, name):
		device = self.devices[name]
		
		#hack
		partCount = device[2][1]		
		for i in range(1, partCount+1):
			self.mainWindow.core.log('info: Im on part number '+str(i))

			#2 = index
			#3 = first pos
			#4 = current pos
			pitch = device[2][0]
			currentIndex = device[2][2]
	
			# simulation of X- type
			xPick = device[2][3][0]-pitch*(currentIndex-1)
			yPick = device[2][3][1]
			pickPos = [xPick, yPick]
			
			self.mainWindow.machine.goTo(pickPos, 2000)
			time.sleep(2)
			QtGui.QApplication.processEvents()
			self.mainWindow.on_btnLoadCCD_clicked()

			#update current index
			self.devices[name][2][2] = self.devices[name][2][2]+1
		self.devices[name][2][2] = 1














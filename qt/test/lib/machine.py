import serial
import pprint as pp
import time

class Machine:

	def __init__(self, mainWindow):
		self.mainWindow = mainWindow

		self.queue = []

		self.connected = False
		self.port = '/dev/ttyACM0' # default port value
		#self.connect()

	def connect(self, port):
		self.port = port
		try:
			self.serial = serial.Serial(self.port, 115200, timeout=0)
		#if self.serial:
			time.sleep(2)
			self.serial.flushInput()
			self.connected = True
			return True
		#else:
		#	return False

		except serial.SerialException:

			print 'Machine.Connect(): Unable to open the serial port!'
			return False

	def isConnected(self):
		if self.connected is True:
			return True
		else:
			return False


	def disconnect(self):
		self.serial.close()
		self.connected = False

	def dumpQueue(self):
		pp.pprint(self.queue)

	def isQueueEmpty(self):
		if len(self.queue) == 0:
			pp.pprint('Machine queue is empty.')
			return True
		else:
			pp.pprint('Machine queue is NOT empty.')
			pp.pprint(len(self.queue))
			return False

	def write(self, gcode):
		self.serial.write(gcode+'\r')

	def read(self):
		line = self.serial.readline()
		line = line.strip()
		pp.pprint(line.strip())
		return line

	def currentPos(self):

		self.serial.flushInput()
		# hack TODO fix me. Sometimes reading M114 failed
		self.write('M400')
		while self.read() != 'ok':
			pass
		# end of hack

		self.write("M114")
		#pos = self.read()
		while True:
			pos = self.read()
			if pos.startswith('ok') is False:
				pass

			else:
				break
		
		#pp.pprint(pos)

		xstart = pos.find('X');
		xend = pos.find(' ', xstart)

		ystart = pos.find('Y');
		yend = pos.find(' ', ystart)

		x = float(pos[xstart+2:xend])
		y = float(pos[ystart+2:yend])
		posXY = [x, y]
		#pp.pprint(posXY)
		#pp.pprint(xend)
		#pp.pprint(pos[xstart+2:xend])

		return posXY

	def relMove(self, axis, value, speed):
		gcode = 'G0 '+axis+str(value)+' F'+str(speed) 
		self.addToQueue('G91')
		self.addToQueue(gcode)
		self.addToQueue('G90')
		self.dumpQueue()
		self.run()

	def goTo(self, pos, speed):
		pass
		gcode = 'G0 X'+str(pos[0]) + ' Y'+ str(pos[1])+ ' F'+str(speed) 
		self.addToQueue('G90')
		self.addToQueue(gcode)
		self.dumpQueue()
		self.run()

	def valveOpen(self):
		self.addToQueue('M43')	
	
	def valveClose(self):
		self.addToQueue('M42')	
	
	def pick(self, z = None):
		if z == None:
			self.addToQueue('G30') # jed dolu dokud nesepne vyskovy sensor
		else:
			self.addtoQueue('G0 Z' + str(z) ) # jdi v ose Z na danou vysku	
		self.valveOpen()
		self.run()

	def place(self):
		self.addToQueue('G30')
		self.valveClose()
		self.run()

	def vacCheck(self):


		import logging
		import time
		logger = logging.getLogger('myapp')
		hdlr = logging.FileHandler('/var/tmp/myapp.log')
		formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
		hdlr.setFormatter(formatter)
		logger.addHandler(hdlr) 
		logger.setLevel(logging.WARNING)

		i = 0
		self.valveClose()
		self.run()
		time.sleep(2)
		while True:
			pressure = self.getResponse('M105')

			i=i+1

			if i == 25:
				self.valveOpen()
				self.run()
				time.sleep(0.5)
			#raw = None
			#RAW value from DAC 0-4096
			end = pressure.find('.0')
			pp.pprint(end)
			raw = pressure[5:end]
			pp.pprint(raw)
			progressbar = 100 - ((4096-int(raw))/4096)*100
			self.mainWindow.barVac.setValue(progressbar)
		
	
			self.mainWindow.core.log('Vacuum: '+ str(raw))	
		
			logger.error('RAW:'+str(raw))	
			time.sleep(0.2)

			if i == 80:
				time.sleep(0.5)
				self.valveClose()
				self.run()
				time.sleep(0.5)
			if i>100:
				break


	def home(self):
		self.addToQueue('G28')
		self.dumpQueue()
		self.run()

	def addToQueue(self, gcode):
		self.queue.append(gcode)

	def getResponse(self, gcode):
		if self.isQueueEmpty() is True:
			self.write(gcode)
			while True:
				read =  self.read()
				if read.startswith('ok'):
					pp.pprint('Machine:getResponse(gcode): '+ read )	
					return read					

		else:
			pp.pprint('Machine:getResponse(gcode): Queue is notempty. Try again.')	
			return None		


	def runRepeatability(self):

		self.goTo( (290, 290), 4000)
		self.goTo( (150, 150), 4000)

		image = self.mainWindow.core.getTopImage()
		image.save('0.png', format=None, quality=-1)

		self.goTo( (290, 290), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('1.png', format=None, quality=-1)


		self.goTo( (290, 225), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('2.png', format=None, quality=-1)


		self.goTo( (290, 150), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('3.png', format=None, quality=-1)


		self.goTo( (290, 75), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('4.png', format=None, quality=-1)


		self.goTo( (290, 10), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('5.png', format=None, quality=-1)


		self.goTo( (225, 10), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('6.png', format=None, quality=-1)


		self.goTo( (150, 10), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('7.png', format=None, quality=-1)


		self.goTo( (75, 10), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('8.png', format=None, quality=-1)


		self.goTo( (10, 10), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('9.png', format=None, quality=-1)


		self.goTo( (10, 75), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('10.png', format=None, quality=-1)


		self.goTo( (10, 150), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('11.png', format=None, quality=-1)


		self.goTo( (10, 225), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('12.png', format=None, quality=-1)


		self.goTo( (10, 290), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('13.png', format=None, quality=-1)


		self.goTo( (75, 290), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('14.png', format=None, quality=-1)


		self.goTo( (150, 290), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('15.png', format=None, quality=-1)


		self.goTo( (225, 290), 4000)
		self.goTo( (150, 150), 4000)
		image = self.mainWindow.core.getTopImage()
		image.save('16.png', format=None, quality=-1)


		pass


	def run(self):
		if self.isQueueEmpty() is False:
			#pp.pprint('lol')
			for gcode in self.queue[:]:

				self.write(gcode)
				#pp.pprint(self.read())

				#if response != "ok":

#					response = self.read()
#					print('response: ' + response)
#					if response.startswith('ok'):
#						print('looser')
#						break
#					else:
#						print('big looser')		
				while True:
					response = self.read()
					if response.startswith('ok'):
						break

#				while self.read().startswith('ok'):
#					pass

					
#				response = self.read()
#				if response.startswith('ok') is False:
#					pp.pprint('Dude, something went wrong: '+response)
#					response = self.read()
#				#raise ValueError('run(): Incorrect response from machine!')
			
				self.queue.remove(gcode)

			self.write('M400')
			while self.read() != 'ok':
				pass
			pp.pprint('run(): All movements are completed.')
			self.serial.flushInput()
		else:
			pp.pprint('run(): Nothing to do. Queue is empty.')

'''
	def isConnected(self):
		if self.serial.isOpen():
			return True
		else:
			return False
'''


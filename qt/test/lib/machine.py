import serial
import pprint as pp
import time

class Machine:

	def __init__(self):

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


	def addToQueue(self, gcode):
		self.queue.append(gcode)

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

				while self.read().startswith('ok'):
					pass

					
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
'''
machine = Machine('/dev/ttyACM0')
#machine.dumpQueue()
#machine.run()
#machine.isQueueEmpty()
machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
#machine.addToQueue('M114')
machine.dumpQueue()
#machine.write('version\r\n')
#machine.read()
machine.run()

machine.addToQueue('M105')
machine.addToQueue('G1 X0 Y0 F11000')
#machine.addToQueue('M114')
machine.dumpQueue()
#machine.write('version\r\n')
#machine.read()
machine.run()

machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M114')
machine.addToQueue('M114')
machine.run()






machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M105')
machine.dumpQueue()
machine.run()

machine.addToQueue('M105')
machine.addToQueue('G1 X0 Y0 F11000')
machine.addToQueue('M114')
machine.dumpQueue()
machine.run()

machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M114')
machine.addToQueue('M114')
machine.run()
machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M105')
machine.dumpQueue()
machine.run()

machine.addToQueue('M105')
machine.addToQueue('G1 X0 Y0 F11000')
machine.addToQueue('M114')
machine.dumpQueue()
machine.run()

machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M114')
machine.addToQueue('M114')
machine.run()
machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M105')
machine.dumpQueue()
machine.run()

machine.addToQueue('M105')
machine.addToQueue('G1 X0 Y0 F11000')
machine.addToQueue('M114')
machine.dumpQueue()
machine.run()

machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M114')
machine.addToQueue('M114')
machine.run()

machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M105')
machine.dumpQueue()
machine.run()

machine.addToQueue('M105')
machine.addToQueue('G1 X0 Y0 F11000')
machine.addToQueue('M114')
machine.dumpQueue()
machine.run()

machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M114')
machine.addToQueue('M114')
machine.run()

machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M105')
machine.dumpQueue()
machine.run()

machine.addToQueue('M105')
machine.addToQueue('G1 X0 Y0 F11000')
machine.addToQueue('M114')
machine.dumpQueue()
machine.run()

machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M114')
machine.addToQueue('M114')
machine.run()

machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M105')
machine.dumpQueue()
machine.run()

machine.addToQueue('M105')
machine.addToQueue('G1 X0 Y0 F11000')
machine.addToQueue('M114')
machine.dumpQueue()
machine.run()

machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M114')
machine.addToQueue('M114')
machine.run()

machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M105')
machine.dumpQueue()
machine.run()

machine.addToQueue('M105')
machine.addToQueue('G1 X0 Y0 F11000')
machine.addToQueue('M114')
machine.dumpQueue()
machine.run()

machine.addToQueue('M114')
machine.addToQueue('G1 X500 Y500 F11000')
machine.addToQueue('M114')
machine.addToQueue('M114')
machine.run()





















machine.disconnect()

'''


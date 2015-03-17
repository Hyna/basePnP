import numpy as np
import pprint
import math


# documentation: none

# tests: No tests at all


class Core:
	'setup'

	def __init__(self):
		self.version = '0.1 alpha'

		# TODO Load these values from file
		self.topPixelPermm = 30.5 # top camer pixel per mm
		self.bottomPixelPermm = 666 #bottom camera pixel per mm
		self.boardOffset = [40,50] # X,Y position where 0,0 of board is. Board workplace
		

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

'''
core = Core()
version = core.getVersion()
pprint.pprint(version)

test = core.toPix(4, 0)
pprint.pprint(test)

test2 = core.tomm(10, 0)
pprint.pprint(test2)
'''

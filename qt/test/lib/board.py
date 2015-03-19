

class Board:
	'board alignmentm'


	def __init__(self, mainWindow):
		self.mainWindow = mainWindow
		self.aligned = False
		self.mode = 1 # mode 1 means Manual Zero position - no fiducials
		self.boardOffset = [6,245]

	def setBoardOffset(self, offset):
		self.boardOffset = offset


	def mode1(self):
		self.aligned = True
		self.mainWindow.lblBoardStatus.setText('Board is aligned in MODE1.')
		pass

	def clear(self):
		self.aligned = False
		self.mainWindow.lblBoardStatus.setText('Board is NOT aligned.')

	def transform(self, pos):
		if self.mode == 1:

			xnew = self.boardOffset[0] + pos[0]
			ynew = self.boardOffset[1] + pos[1]
			newpos = [xnew , ynew]
			return newpos
		else:
			return value



from locker import Locker

class Lockio:

	def __init__(self,id):
		self.id = id
		self.lockers = []

	def addLocker(self,locker: Locker):
		self.lockers.append(locker)

	def addLockers(self, lockers):
		for locker in lockers:
			self.lockers.append(locker)

	def switchOnGreenAll(self):
		for locker in self.lockers:
			locker.switchOnGreen()

	def switchOffGreenAll(self):
		for locker in self.lockers:
			locker.switchOffGreen()

	def switchOnRedAll(self):
		for locker in self.lockers:
			locker.switchOnRed()

	def switchOffRedAll(self):
		for locker in self.lockers:
			locker.switchOffRed()

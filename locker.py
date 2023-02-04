import RPi.GPIO as GPIO

class Locker:
	
	def __init__(self,id,redGPIOPin,greenGPIOPin):
		self.id = id
		self.redGPIOPin = redGPIOPin
		self.greenGPIOPin = greenGPIOPin
		GPIO.setup([greenGPIOPin,redGPIOPin],GPIO.OUT)

	def switchOnGreen(self):
		GPIO.output(self.greenGPIOPin,True)

	def switchOffGreen(self):
		GPIO.output(self.greenGPIOPin,False)

	def switchOnRed(self):
		GPIO.output(self.redGPIOPin,True)

	def switchOffRed(self):
		GPIO.output(self.redGPIOPin,False)

	def switchOff(self):
		self.switchOffGreen()
		self.switchOffRed()

import RPi.GPIO as GPIO
class Fly:

  def __init__(self, pin):
    self.pin = pin
    self.intensity = 0
    self.__setup()

  def __setup(self):
    GPIO.setup(self.pin, GPIO.OUT)
    self.output = GPIO.PWM(self.pin,500)
    self.output.start(self.intensity)

  def getPin(self):
    return self.pin

  def getIntensity(self):
    return self.intensity

  def setIntensity(self, intensity):
      self.intensity = intensity

  def paint(self):
    self.p.ChangeDutyCycle(intensity)

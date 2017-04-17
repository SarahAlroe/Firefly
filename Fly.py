import RPi.GPIO as GPIO
class Fly:

  def __init__(self, pin):
    self.pin = pin
    self.intensity = 0
    self.__setup()
    self.__update()

  def __setup(self):
    GPIO.setup(self.pin, GPIO.OUT)
    self.output = GPIO.PWM(self.pin,100)
    self.output.start(self.intensity)

  def getPin(self):
    return self.pin

  def getIntensity(self):
    return self.intensity

  def setIntensity(self, intensity):
      self.intensity = intensity
      self.__update()

  def paint(self):
      if(self.is_updated):
        self.output.ChangeDutyCycle(self.intensity)
        self.is_updated = False

  def __update(self):
      self.is_updated = True

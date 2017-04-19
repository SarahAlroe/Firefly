import RPi.GPIO as GPIO
from Insect import *

class Fly( Insect ):

  def __init__(self, pin):
    Insect.__init__(self)
    self.pin = pin
    self.__setup()

  def __setup(self):
    GPIO.setup(self.pin, GPIO.OUT)
    intensity = self.getIntensity() * 100
    self.output = GPIO.PWM(self.pin, 500)
    self.output.start(intensity)

  def getPin(self):
    return self.pin

  def paint(self):
      intensity = self.getIntensity() * 100
      #print str(intensity)
      self.output.ChangeDutyCycle(intensity)

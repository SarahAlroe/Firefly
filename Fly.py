import RPi.GPIO as GPIO
class Fly:
  def __init__(self, pin, intensity=0):
    self.pin=pin
    self.intensity=intensity
    self.p = GPIO.PWM(pin,500)
    self.p.start(intensity)
    
  def getPin(self):
    return self.pin
  def getNumber(self):
    return getPin()
  def getIntensity(self):
    return self.intensity
  def setIntensity(self, intensity):
    self.intensity = intensity
    self.p.ChangeDutyCycle(intensity)

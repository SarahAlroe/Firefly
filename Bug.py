from neopixel import *
from Insect import *
class Bug( Insect ):

  def __init__(self, strip, number):
    Insect.__init__(self)
    self.strip = strip
    self.number = number

    self.color = (0,0,0)
  
  def getNumber(self):
    return self.number

  def setColor(self, color):
      self.color = color
  
  def getColor(self):
    return self.color


  def paint(self):
      n = self.getIntensity()
      c = Color(int(self.color[0]*n), int(self.color[1]*n), int(self.color[2]*n))
      self.strip.setPixelColor(self.getNumber(), c)

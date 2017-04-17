from neopixel import *

class Bug:

  def __init__(self, strip, number):
    self.strip = strip
    self.number = number

    self.animCounter = 0
    self.color = (0,0,0)
    self.intensity = 0
    self.__update()

  
  def getNumber(self):
    return self.number

  def setColor(self, color):
      self.color = color
      self.__update()
  
  def getColor(self):
    return self.color

  def setIntensity(self, intensity):
      self.intensity = intensity
      self.__update()

  def getIntensity(self):
      return intensity

  def paint(self):
      if self.is_updated:
        c = Color(self.color[0], self.color[1], self.color[2], self.intensity)
        self.strip.setPixelColor(self.getNumber(), c)
        is_updated = False

  def __update(self):
      self.is_updated = True

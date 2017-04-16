from neopixel import *
class Bug:
  def __init__(self, number, intensity = 0, red = 0, green = 0, blue=0):
    #intensity = 0
    #red = 0
    #green = 0
    #blue = 0

    self.number = number
    self.intensity = intensity
    self.origColor = Color(red,green,blue)
    self.cColor = self.origColor
    self.animCounter = 0
  
  def getNumber(self):
    return self.number
  
  def getColor(self):
    return self.cColor
  

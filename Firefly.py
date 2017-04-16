#Ey boss, launch this one.
import time
import RPi.GPIO as GPIO
from neopixel import *
from Bug import *
from Fly import *

#CONST
LED_COUNT      = 6             # Number of LED pixels.
LED_PIN        = 18            # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000        # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5             # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255           # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False         # True to invert the signal (when using NPN transistor level shift)
FLY_PINS       = [16,22,32,36] # Pins on which flies are connected.

#DEFS
def updateBugs():
  #TODO: Consider doing this directly in the bug class similar to fly
  for bug in bugs:
    #update strip
    strip.setPixelColor(bug.getNumber(),bug.getColor())
  strip.show()

#RUN
if __name__ == '__main__':
  #Lists
  bugs = []
  flies = []
  
  #Init neopixels
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
  strip.begin()

  #Init buglist
  for i in range(LED_COUNT):
    bugs.append(Bug(i))
  
  #Init flylist
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(FLY_PINS, GPIO.OUT)
  for f in FLY_PINS:
    flies.append(Fly(f,40))
    #Set GPIO

  #Run Loop
  try:
    while True:
      updateBugs()
      time.sleep(0.1)
  except KeyboardInterrupt:
    pass
  GPIO.cleanup()

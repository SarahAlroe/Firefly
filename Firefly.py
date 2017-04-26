#Ey boss, launch this one.
import time
import RPi.GPIO as GPIO
from neopixel import *
from Bug import *
from Fly import *
from SimplePulseBehaviour import *
from FlyBehaviour import *

#CONST
LED_COUNT      = 6             # Number of LED pixels.
LED_PIN        = 18            # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000        # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5             # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 128           # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False         # True to invert the signal (when using NPN transistor level shift)
FLY_PINS       = [16,22,32,36] # Pins on which flies are connected.

animation_count = 0

#DEFS

def animateAll():

    global animation_count 
    animation_count += 1
    for bug in bugs:
        bug.setColor((255,255,0))
        bug.behave()

    for fly in flies:
        fly.behave()

def paintAll():
  for bug in bugs:
    bug.paint()
  strip.show()

  for fly in flies:
    fly.paint()

#RUN
if __name__ == '__main__':
  #Lists
  bugs = []
  flies = []
  
  #Init neopixels
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
  strip.begin()

  #Init buglist
  for led_number in range(LED_COUNT):
    bug = Bug(strip, led_number)
    bug.setBehaviour(SimplePulseBehaviour(bug))
    bugs.append(bug)
  
  #Init flylist
  GPIO.setmode(GPIO.BOARD)
  for pin in FLY_PINS:
    fly = Fly(pin)
    fly.setBehaviour(FlyBehaviour(fly))
    flies.append(fly)

  #Run Loop
  try:
    while True:
      animateAll()
      paintAll()
      time.sleep(0.04) #25 fps
  except KeyboardInterrupt:
    pass
  #Clean exit
  for bug in bugs:
    bug.setColor((0,0,0))
    bug.paint()
  strip.show()
  GPIO.cleanup()

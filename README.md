# Firefly
_The premier pet rock solution_  
Firefly is a python controler for neopixels and leds on Raspberry Pi, emulating _cyber_-fireflies in a jar.
It will eventually be able sync changes in ligting across multiple clients and support interactivity.
## Notes to self  
* 6 bugs are connected on pin 12 (BCM 18)
* Flies are connected on pins 16,22,32 and 36
* Intensity for bugs and flies is 0.0 - 100.0
* Flies automatically update intensity when changed, Bugs don't yet.
* Fly pcm is at 100 hZ currently. Is this ok?

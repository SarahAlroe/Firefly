# Firefly
_The premier pet rock solution_  
Firefly is a python controler for neopixels and leds on Raspberry Pi, emulating _cyber_-fireflies in a jar.
It will eventually be able sync changes in ligting across multiple clients and support interactivity.

## Server interaction
Get update: `[site root] `  
Response: `{"activity":"XX","bugs":["{\"r\":XX,\"g\":XX,\"b\":XX}",(...)]}`  

Control:
Reset server: `[site root]/setup/?bugs=XX`  
Set bug color: `[site root]/set/?bug=xx[&r=XX][&g=XX][&b=XX]` (rgb optional, if not set uses previous value.)
Set activity: `[site root]/set/?activity=xx[&ttl=XX]` (ttl in seconds, defaults to 20)

## Update service params
Send state of system:
`sysStatSend.sh [pixel nr]`

Send devices on network:
`networkDeviceSend.sh [pixel nr] [MAC r] [MAC g] [MAC b]`

## Dependencies
Client:
* Python
* Neopixel library

Server:
* PHP
* Redis

Update Services:
* grep
* awk
* free
* hdparm
* curl

## Notes to self  
* 6 bugs are connected on pin 12 (BCM 18)
* Flies are connected on pins 16,22,32 and 36
* Intensity for bugs and flies is 0.0 - 100.0
* Flies automatically update intensity when changed, Bugs don't yet.
* Fly pcm is at 100 hZ currently. Is this ok?

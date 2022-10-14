'''
I found in blogs than built-in led is
2 or 21 in TTGO (ESP32-WROVER-B)
But didn't work for me, I found that 5 is
the built-in led
'''


from machine import Pin # get the Pin class
from time import sleep # add sleep function

led = Pin(5, Pin.OUT) # set Pin 5 as out mode


while True:
  led.value(not led.value()) # set the opposite value
  sleep(0.5) # sleep 0.5 seconds

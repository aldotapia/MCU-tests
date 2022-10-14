'''
With a multimeter, testing different
pins to be sure about the number index
the board
'''


from machine import Pin # get the Pin class
from time import sleep # add sleep function

pin15 = Pin(15, Pin.OUT)
pin2 = Pin(2, Pin.OUT)
pin0 = Pin(0, Pin.OUT)
pin4 = Pin(4, Pin.OUT)
pin16 = Pin(16, Pin.OUT) # unavailable
pin17 = Pin(17, Pin.OUT) # unavailable

while True:
  pin15.value(not pin15.value()) # set the opposite value
  pin2.value(not pin2.value()) # set the opposite value
  pin0.value(not pin0.value()) # set the opposite value
  pin4.value(not pin4.value()) # set the opposite value
  # pin16.value(not pin16.value()) unavailable
  # pin17.value(not pin17.value()) unavailable
  sleep(2) # sleep 2 seconds

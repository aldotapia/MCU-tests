# MCU-tests

## Teensy 4.0

### Blink:

The most basic test to check if the board is working. It blinks the LED on the board.

````
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.5)
````

### UART communitacion between two boards:

Sender:
```

```

Receiver:
```
import busio
import board
import time

uart = busio.UART(board.TX2, board.RX2, baudrate=9600, timeout=0)

print('started!')

while True:
    byte_read = uart.read(1)
    if byte_read is None:
        continue

    if byte_read == b"<":
        message = []
        message_started = True
        continue

    if message_started:
        if byte_read == b">":            
            message_parts = "".join(message).split(",")
            message_type = message_parts[0]
            message_started = False
            print(message_parts[1])
            
        else:
            message.append(chr(byte_read[0]))
```
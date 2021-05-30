#
# Special edition for LC Technology relay 1x
# With CPU STC15F104W
#
import time
import ubinascii

from machine import Pin, Signal
from machine import UART

led_pin = Pin(2, Pin.OUT)
led = Signal(led_pin, invert=True)

ut0 = UART(0, 9600)
ut0.init(9600, bits=8, parity=None, stop=1)

def toggle(p):
	p.value(not p.value())

def on():
    ut0.write(ubinascii.unhexlify('A00101A2'))    

def off():
    ut0.write(ubinascii.unhexlify('A00100A1'))
 
def test():
    while True:
                time.sleep(5.0)
                print('Start')
                while True:
                    print('relay on')
                    on()
                    time.sleep(1.0)
                    print('relay off')
                    off()
                    time.sleep(1.0)
        

test()

#while True:
#	toggle(led)
# below will turn the relay on:
#	ut0.write(ubinascii.unhexlify('A00101A2') )
#	rele_on()
#	led.value(1)
#	time.sleep_ms(1000)ut
# below will turn the relay off:
#	ut0.write(ubinascii.unhexlify('A00100A1') )
#	rele_off()
#	led.value(0)
#	time.sleep_ms(1000)

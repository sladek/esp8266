#
# This suprisingly works on stock boards. 
# Tested on LC Technology Esp8266 Relay x2 and x4 with CPU MS51FB9AE
# Make sure that the board is Mode 2 (Red LED is on)
# If blue LED is on when the boar is powered up, 
# then disconnect the power, push S1 button and power the board.
# This will swith the board to Mode 2
# If everything works, then green LED on the LCTech board will 
# start blinking at the interval of 1s.
#
import time
import ubinascii

from machine import Pin, Signal
from machine import UART

led_pin = Pin(2, Pin.OUT)
led = Signal(led_pin, invert=True)

ut0 = UART(0, 115200)
ut0.init(115200, bits=8, parity=None, stop=1)

def toggle(p):
	p.value(not p.value())

def cpu_connect():
    ut0.write('\r\n0,CONNECT\r\n+IPD,0,4:')
    
def cpu_disconnected():
    ut0.write('0,CLOSED\r\n')

def on1():
    cpu_connect()
    ut0.write(ubinascii.unhexlify('A00101A2'))    
    cpu_disconnected()

def off1():
    cpu_connect()
    ut0.write(ubinascii.unhexlify('A00100A1'))
    cpu_disconnected()

def on2():
    cpu_connect()
    ut0.write(ubinascii.unhexlify('A00201A3'))    
    cpu_disconnected()

def off2():
    cpu_connect()
    ut0.write(ubinascii.unhexlify('A00200A2'))
    cpu_disconnected()

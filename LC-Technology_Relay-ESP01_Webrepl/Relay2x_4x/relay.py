#
# This suprisingly works on stock boards. 
# Tested on LC Technology Esp8266 Relay x2 and x4 with CPU MS51FB9AE
# Make sure that the board is Mode 2 (Red LED is on)
# If blue LED is on when the boar is powered up, 
# then disconnect the power, push S1 button and power the board.
# This will swith the board to Mode 2
# If everything works, then green LED on the LCTech board will 
# start blinking at the interval of 1s and the relays will also 
# swich on/off in 1 second's intervals, one by one.
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

def on3():
    cpu_connect()
    ut0.write(ubinascii.unhexlify('A00301A4'))    
    cpu_disconnected()

def off3():
    cpu_connect()
    ut0.write(ubinascii.unhexlify('A00300A3'))
    cpu_disconnected()

def on4():
    cpu_connect()
    ut0.write(ubinascii.unhexlify('A00401A5'))    
    cpu_disconnected()

def off4():
    cpu_connect()
    ut0.write(ubinascii.unhexlify('A00400A4'))
    cpu_disconnected()

 
def ready():
    ut0.write('\r\nready\r\n')
    
def test():
#    ut0.write('\r\n\r\n')
    s_flag = ''
    while True:
        if ut0.any():
            u_read = ut0.read()
            s_read = str(u_read)
#            print(s_read)
#            print('s_flag = ' + s_flag)
#            if(s_read.find('AT+CWMODE') != -1):
#                s_flag = 'CWMODE'
#                ut0.write('AT+CWMODE=1\r\n')
#                ut0.write('OK\r\n')
            if(s_read.find('AT+RST') != -1):
#                ut0.write('AT+CWMODE=1\r\n')
#                ut0.write('AT+RST\r\n')
#                ut0.write('WIFI CONNECTED\r\n')
#                ut0.write('WIFI GOT IP\r\n')
#                ut0.write('AT+CIPMUX=1\r\n')
#                ut0.write('AT+CIPSERVER=1,8080\r\n')
#                ut0.write('AT+CIPSTO=360\r\n')

                time.sleep(5.0)
                print('Start')
                while True:
#                    if ut0.any():
#                        u_read = ut0.read()
#                        print(str(u_read))
                    print('relay 1')
                    on1()
                    time.sleep(1.0)
                    off1()
                    time.sleep(1.0)

                    print('relay 2')
                    on2()
                    time.sleep(1.0)
                    off2()
                    time.sleep(1.0)

                    print('relay 3')
                    on3()
                    time.sleep(1.0)
                    off3()
                    time.sleep(1.0)

                    print('relay 4')
                    on4()
                    time.sleep(1.0)
                    off4()
                    time.sleep(1.0)
        
def echo():
    while True:
        if ut0.any():
            u_read = ut0.read()
            s_read = str(u_read)
            ut0.write(s_read)
    

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

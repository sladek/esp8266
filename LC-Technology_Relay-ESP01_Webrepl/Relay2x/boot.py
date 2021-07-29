# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
import network
import uos
uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
import ubinascii
import time
import machine

webrepl.start()
gc.collect()

# Here is placed some configuration 
# Wifi credentials
ssid = 'REPLACE_WITH_YOUR_SSID'
password = 'REPLACE_WITH_YOUR_PASSWORD'
# Here is placed configuration of mqtt. 
# You can use IP address or the name like: 'broker.hivemq.com'
mqtt_server = 'REPLACE_WITH_YOUR_MQTT_BROKER_IP'
# Here you can define topic name for each relay
# like in the following example. You can choose completely 
# different name for each topic 
topic_relay1 = b'/myhome/relay_boards/board2x/relay1'
topic_relay2 = b'/myhome/relay_boards/board2x/relay2'
topic_pub = b'/myhome/relay_boards/board2x/status'

last_message = 0
message_interval = 5
counter = 0

client_id = ubinascii.hexlify(machine.unique_id())

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

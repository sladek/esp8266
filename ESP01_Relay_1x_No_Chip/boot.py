import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'PLACE_YOUR_SID_HERE'
password = 'PLACE_WIFI_PASSWORD_HERE'
mqtt_server = 'PLACE_IP_OR_NAME_OF_YOUR MQTT_SERVER'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'/myhome/relay/command'
topic_pub = b'/myhome/relay/status'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())


  GNU nano 4.8                                 /tmp/tmp58pr1txi/main.py                                           
# Complete project details at https://RandomNerdTutorials.com

led = machine.Pin(2, machine.Pin.OUT)
led.value(1)

relay = machine.Pin(0, machine.Pin.OUT)
relay.value(1)

def led_on():
  led.off()

def led_off():
  led.on()

def relay_on():
  relay.off()

def relay_off():
  relay.on()

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == topic_sub and msg == b'1':
    relay_on()
  if topic == topic_sub and msg == b'0':
    relay_off()

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

led_on()
while True:


from umqttsimple import MQTTClient
import machine
import ubinascii
import time
import relay

# call back function for received message from MQTT server
def sub_cb(topic, msg):                                                                                                                           
    print((topic, msg))       
    if topic == topic_relay1: 
        if msg == b'on' or msg == b'1':
            relay.on1()
        else:
            relay.off1()
    if topic == topic_relay2: 
        if msg == b'on' or msg == b'1':
            relay.on2()
        else:
            relay.off2()


# Connection to MQTT server and subscription to topic for each relay            
def connect_and_subscribe():
    global client_id, mqtt_server
    global topic_relay1, topic_relay2
    client = MQTTClient(client_id, mqtt_server)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_relay1)
    client.subscribe(topic_relay2)
    print('Connected to %s MQTT broker')
    return client

# This function causes the reset in case of disconnection from MQTT or other errors
def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()
  
# The following try block tries to do initial connection to MQTT
try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()

# And finally here is main loop in which mqtt client is checked for incomming messages
while True:
    try:
        client.check_msg()
    except OSError as e:
        restart_and_reconnect()

import paho.mqtt.client as mqtt
import numpy as np

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")

def on_message(client, userdata, message):
    print('Received message: "' + str(message.payload) + '" on topic "' + message.topic + '" with QoS ' + str(message.qos))

client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect_async('test.mosquitto.org')

client.loop_start()

thing = [1, 1, 2, 3, 5, 8, 13]

client.publish('ece180d/test', 'Hello from team 1!', qos=1)
client.publish('ece180d/test', 'I hope you are doing well today!', qos=1)
client.publish('ece180d/test', 'here is the fibbonaci you ordered: ' + str(thing), qos=1)

client.loop_stop()
client.disconnect()

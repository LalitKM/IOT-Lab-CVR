import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("localhost",1883)
while True:
	data = input("Enter msg : ")
	client.publish("rfid", data);
client.disconnect();

import paho.mqtt.client as mqtt
import mysql.connector
import win32com.client as wincl


def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("rfid")

def on_message(client, userdata, msg):
  print((msg.payload.decode()))
  '''mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="iotdashb"
  )
  
  mycursor = mydb.cursor()
  sql = "select name from register where rfid = '"+str(msg.payload.decode())+"'"
  print(sql)
  hel = mycursor.execute(sql)
          
  myresult = mycursor.fetchone()

  hello = str(myresult[0])'''
  speak = wincl.Dispatch("SAPI.SpVoice")
  if str(msg.payload.decode()) == "c0":
    speak.Speak("Welcome Lalit")
  if str(msg.payload.decode()) == "14":
    speak.Speak("Welcome Ashish")


  
      

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)

client.loop_forever()


      
  
    

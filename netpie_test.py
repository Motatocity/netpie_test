import microgear.client as client
import time

gearkey = "3Pz59oJzsIRox0g"
gearsecret =  "DqOZKONNM0Hk9HZOwqc1e96FTzRIHs"
appid = "motatocity"

client.create(gearkey,gearsecret,appid,{'debugmode': True})

def connection():
    print ("Now, I am connected with netpie")

def subscription(topic,message):
    print (topic+" "+message)

def callback_message(topic, message) :
    print ("I got message from ", topic, ": ", message)

client.setname("doraemon")
client.on_connect = connection
client.on_message = subscription
client.on_message= callback_message
client.subscribe("/chat")

client.connect()

while True:
    #client.chat("doraemon","Hello world. "+str(int(time.time())))
    client.on_message= callback_message
    time.sleep(2)

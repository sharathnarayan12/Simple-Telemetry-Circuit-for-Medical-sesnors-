import serial
import time
import thingspeak
import pyrebase
from twilio.rest import Client
#import firebase
channel_id = 1211863
read_key ='K1FJFQPPHZ8QWZEO'
ser = serial.Serial('COM6',115200)
channel = thingspeak.Channel(id=channel_id, api_key=read_key)
config = {
  "apiKey": "AIzaSyCse3HpG_aSAMoCZ468TVDsWfgTqGCjlAs",
  "authDomain": "rt-heart-pluse-analysis.firebaseapp.com",
  "databaseURL": "https://rt-heart-pluse-analysis-default-rtdb.firebaseio.com/",
  "storageBucket": "rt-heart-pluse-analysis.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
account_sid = 'ACddd892bad27fe97f17d7140b5adbbcad' 
auth_token = '3ef7ab34695b233f16410db06f56b607'
client = Client(account_sid, auth_token) 
while 1:
     data= ser.readline().rstrip()
     print(" heart rate :"+ str(data))
     response = channel.update({'field1':data})
     data1={"heart_rate":str(data)}
     db.child("real time data").child("1-set").set(data1)
     message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=("heart_pluse of patient :"+str(data)),      
                              to='whatsapp:+917619398922' 
                          )                   
     print(message.sid)
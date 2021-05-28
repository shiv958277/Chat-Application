# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.dispatch.dispatcher import receiver
from .models import Message, registration,tra,person
from asgiref.sync import sync_to_async
from datetime import datetime

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'communication_%s' % self.room_name
        print(self.room_group_name)

        print(2)
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
           
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
            
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username=text_data_json['username']
        room=text_data_json['room']
        # room=text_data_json['room-name-input']
        

        time=await self.save_message(username,room,message)
        time=str(time)
        


        
      
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username':username,
                'room':room,
                'time':time,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username=event['username']
        room=event['room']
        time=event['time']
        print(time)
        
        # def myconverter(o):
        #     if isinstance(o, time):
        #         return o.__str__()


        


       
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username':username,
            'time':time,
           
        
        }))



    @sync_to_async
    def save_message(self,username,room,message):
        m=Message.objects.create(username=username, room=room, content=message)
        return m.time

    
       
    
##personal chat consumer

class PersonalConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        sender=self.scope['url_route']['kwargs']['user']
        reciever=self.scope['url_route']['kwargs']['username']
        t=await self.check(sender,reciever)
        if t:
            print("exists")

        else:
            p=await self.save_name(self.scope['url_route']['kwargs']['user'],self.scope['url_route']['kwargs']['username'])
            self.roomName=p
            self.room_name="room"+str(self.roomName)
            await self.save(p,self.room_name)
           

        if t==1 or t==0:
            self.room_name=await self.give(sender,reciever)

        elif t==2:
            self.room_name=await self.gi(sender,reciever)

        print("personal connected")
        print(1)
    

        
        # Join room group
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name,
           
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name,
            
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username=self.scope['url_route']['kwargs']['user']
        group=self.room_name
       
        # room=text_data_json['room-name-input']
        time=await self.add(message,username,group)
        time=str(time)
        
        

        


        
      
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message,
                'username':username,
                'time':time,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username=event['username']
        time=event['time']
        print(time)
        
        
        


       
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username':username,
            'time':time
           
        
        }))

    @sync_to_async
    def save_name(self,sender,reciever):
        m=tra.objects.create(sender=sender,reciever=reciever)
        return m.id

    @sync_to_async
    def save(self,id,room):
        m=tra.objects.get(id=id)
        m.room=room
        m.save()

    @sync_to_async
    def check(self,sender,reciever):
        if tra.objects.filter(sender=sender,reciever=reciever).exists():
            return 1

        elif tra.objects.filter(sender=reciever,reciever=sender).exists():
            return 2

        else:
            return 0

    @sync_to_async
    def give(self,sender,reciever):
        x=tra.objects.get(sender=sender,reciever=reciever)
        return x.room
    
    @sync_to_async
    def gi(self,sender,reciever):
        x=tra.objects.get(sender=reciever,reciever=sender)
        return x.room
    
        
    @sync_to_async
    def add(self,message,username,group):
        m=person.objects.create(me=username, group=group, text=message)
        return m.time
    



    

    
       
    



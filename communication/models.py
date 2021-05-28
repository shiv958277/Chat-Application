from django.db import models
from datetime import datetime
# Create your models here.
 

class Message(models.Model):
    username=models.CharField(max_length=255)
    room=models.CharField(max_length=255)
    content=models.TextField()
    time=models.DateTimeField(default=datetime.now)
    

class registration(models.Model):
    UserName=models.CharField(max_length=100,null=True)
    FirstName=models.CharField(max_length=100,null=True)
    LastName=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100,unique=True,primary_key=True)
    Password=models.CharField(max_length=300,null=True)
    image=models.ImageField(null=True,blank=True,upload_to='media/')
    

    def __str__(self):
        return f'{self.Email}'

    
# class privateme(models.Model):
#     sender=models.ForeignKey(registration,on_delete=models.CASCADE)
#     reciever=models.CharField(max_length=100,null=True)
#     msg=models.TextField()
#     time=models.DateTimeField(default=datetime.now)
#     room_name=models.CharField(max_length=100,null=True)


class tra(models.Model):
    sender=models.CharField(max_length=100)
    reciever=models.CharField(max_length=100)
    room=models.CharField(max_length=100,unique=True,null=True)

class person(models.Model):
    me=models.CharField(max_length=100)
    group=models.CharField(max_length=100)
    text=models.TextField()
    time=models.DateTimeField(default=datetime.now)


class Room(models.Model):
    r=models.CharField(max_length=100,unique=True)
    user=models.ForeignKey(registration,on_delete=models.CASCADE)
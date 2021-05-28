from django.shortcuts import render
from .models import Message,registration,tra,person,Room
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers


def index(request):
    u=registration.objects.get(Email=request.session['Email'])
    m=Room.objects.all()
    x=registration.objects.all()
    return render(request, 'index.html',{'u':u,'m':m,'x':x})


def room(request,room_name,username):
    # messages=Message.objects.filter(room=room_name)[0:25]
    
    messages = Message.objects.filter(room=room_name)
    u=registration.objects.get(Email=request.session['Email'])
    try:
        x=registration.objects.filter(UserName=username)
        return render(request, 'room.html', {
                'room_name': room_name,
                'username': username,
                'messages':messages,
                'u':u
                })
            
    except:
        messages.warning('User have not registered yet..')
        return render(request,'index.html',{'messages':messages})


    


def main(request):
    x=registration.objects.all()
    return render(request,'main.html',{'r':x})


def login(request):
    if request.method == 'POST':
        try:
            p=request.POST.get('Password')
            u=registration.objects.get(Email=request.POST.get('Email'))
            if check_password(p,u.Password):
                request.session['Email']=request.POST.get('Email')
                request.session['UserName']=u.UserName
                UserName=request.session['UserName']
                Email=request.session['Email']
            
                return redirect('main')

            else:
                messages.success(request,'Email or Password is invalid')
                

        except registration.DoesNotExist as e:
            messages.success(request,'Email or Password is invalid')
            

    return render(request,'login.html')


def register(request):
    if request.method=='POST' and  request.FILES['image']:
        FirstName=request.POST.get('FirstName')
        LastName=request.POST.get('LastName')
        Email=request.POST.get('Email')
        Password=make_password(request.POST.get('Password'))
        ConfirmPassword=request.POST.get('ConfirmPassword')
        UserName=request.POST.get('UserName')
        image=request.FILES['image']
        registration(FirstName=FirstName,LastName=LastName,UserName=UserName,Email=Email,Password=Password,image=image).save()
        return redirect('login')

    else:
        return render(request,'register.html')
     
    

def logout(request):
    try:
        
        del request.session['Email']
    except:
        x=registration.objects.all()
        return redirect('main.html',{'r':x})

    x=registration.objects.all()
    return render(request,'main.html',{'r':x})


def change(request):
    if request.method=='POST':
        posts=registration.objects.get(Email=request.POST.get('Email'))
        posts.Password=make_password(request.POST.get('Password'))
        posts.save()

        
        messages.success(request,'Password has been Changed Succesfully')
        return redirect('login')

    return render(request,'change.html')



def profile(request):
    r=registration.objects.get(Email=request.session['Email'])
    x=registration.objects.all()
    return render(request,'profile.html',{'r':r,'x':x})

def personal(request,user,username):
    # x=tra.objects.get(sender=user,reciever=username)
    # messages=person.objects.get(group=x.room)
    # u=registration.objects.get(Email=request.session['Email'])
    # try:
    #     return render(request,'person.html',{'user':user,'username':username,'messages':messages,'u':u})

    # except:
    #     messages.warning('User have not registered yet..')
    #     return render(request,'index.html',{'messages':messages})

        if tra.objects.filter(sender=user,reciever=username).exists():
            x=tra.objects.get(sender=user,reciever=username)
            try:
                messages=person.objects.filter(group=x.room)
                u=registration.objects.get(Email=request.session['Email'])
                v=registration.objects.get(UserName=username)
                return render(request,'personal.html',{'user':user,'username':username,'messages':messages,'u':u,'v':v})

            except:
                u=registration.objects.get(Email=request.session['Email'])
                v=registration.objects.get(UserName=username)
                return render(request,'personal.html',{'user':user,'username':username,'u':u,'v':v})
                
        elif tra.objects.filter(sender=username,reciever=user).exists():
            x=tra.objects.get(sender=username,reciever=user)
            try:
                messages=person.objects.filter(group=x.room)
                u=registration.objects.get(Email=request.session['Email'])
                v=registration.objects.get(UserName=username)
                return render(request,'personal.html',{'user':user,'username':username,'messages':messages,'u':u,'v':v})
            except:
                u=registration.objects.get(Email=request.session['Email'])
                v=registration.objects.get(UserName=username)
                return render(request,'personal.html',{'user':user,'username':username,'u':u,'v':v})

        else:
            u=registration.objects.get(Email=request.session['Email'])
            v=registration.objects.get(UserName=username)
            return render(request,'personal.html',{'user':user,'username':username,'u':u,'v':v})



def updateprofile(request):
    u=registration.objects.get(Email=request.session['Email'])
    if request.method=='POST' and  request.FILES['image']:
        u.FirstName=request.POST.get('FirstName')
        u.save()
        u.LastName=request.POST.get('LastName')
        u.save()
        u.Email=request.POST.get('Email')
        u.save()
        u.image=request.FILES['image']
        u.save()
        u.UserName=request.POST.get('UserName')
        u.save()
        messages.success(request,'Profile has been changed Succesfully')
        return render(request,'updateprofile.html')
        
    return render(request,'updateprofile.html')



def createroom(request):
    r=registration.objects.get(Email=request.session['Email'])
    if request.method=="POST":
        x=request.POST.get('ro')
        u=Room()
        u.user_id=r.Email
        u.r=x
        u.save()
        messages.success(request,"Room created successfully")
        return render(request,'profile.html',{'r':r,'messages':messages})
    return render(request,'createroom.html',{'r':r})



def delete(request):
    
    u=registration.objects.get(Email=request.session['Email'])
    u.delete()
    

    return render(request,'main.html')      



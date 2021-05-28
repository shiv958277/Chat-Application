"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from communication.views import main,login,register,change,profile,logout,updateprofile,createroom,delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('communication/', include('communication.urls')),
    path('chat/',include('communication.urls')),
    path('',main,name='main'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('change/',change,name='change'),
    path('profile/',profile,name='profile'),
    path('logout',logout,name='logout'),
    path('updateprofile/',updateprofile,name='updateprofile'),
    path('createroom/',createroom,name='createroom'),
    path('delete/',delete,name='delete'),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/<str:username>/', views.room, name='room'),
    path('personal/<str:user>/<str:username>/',views.personal,name='personal'),
    
]
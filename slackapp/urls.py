from django.urls import path, reverse

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addchannel', views.addchannel, name='addchannel'),  
    path('channeldetail/<int:channel_id>/', views.channeldetail, name='channeldetail'),  
    path('addmessage/<int:channel_id>/', views.addmessage, name='addmessage'),  
    path('joinchannel/<int:channel_id>/', views.joinchannel, name='joinchannel'),  
    path('userlist', views.userlist, name='userlist'),  
    path('addmessageuser/<int:profile_id>/', views.addmessageuser, name='addmessageuser'),  
]
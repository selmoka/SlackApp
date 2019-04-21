from django.urls import path, reverse

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addchannel', views.addchannel, name='addchannel'),  
    path('channeldetail/<int:channel_id>/', views.channeldetail, name='channeldetail'),  
]
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse, Http404
from .models import Channel, Message
from profileapp.models import Profile
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from .forms import ChannelForm


def index(request):
	return render(request, 'channels.html',{
		'channels': Channel.objects.all()
	}) 

def addchannel(request): 
	if request.method == 'POST':
		form = ChannelForm(request.POST)
		if form.is_valid():
			new_channel = form.save(commit=False)
			new_channel.profile=Profile.objects.get(user=request.user)
			print(new_channel)
			new_channel.save()
			return redirect('index')
	else:
	    return render(request, 'addchannel.html', { 'form': ChannelForm })

def channeldetail(request, channel_id):
	return render(request, 'channeldetail.html', { 'channel_id': channel_id })

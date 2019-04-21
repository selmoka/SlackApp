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
	channel = Channel.objects.get(pk=channel_id)
	messages = channel.message_set.all().order_by('-pub_date')
	return render(request, 'channeldetail.html', { 'channel': channel,
		'messages': messages})

def addmessage(request, channel_id): 
	channel = Channel.objects.get(pk=channel_id)
	messages = channel.message_set.all().order_by('-pub_date')
	if request.method == 'POST':
		message = Message()
		message.text = request.POST['text']
		if request.FILES['img']:
			img = request.FILES['img']
			fs = FileSystemStorage(location='media/images', base_url='/media/images')
			filename = fs.save(img.name, img)
			uploaded_file_url = fs.url(filename)
			message.img = uploaded_file_url
		message.profile = Profile.objects.get(user=request.user)
		message.channel = Channel.objects.get(pk=channel_id)
		message.pub_date = datetime.now()
		message.save()
	return render(request, 'channeldetail.html', { 'channel': channel,'messages': messages})

		# channel = Channel.objects.get(pk=channel_id)
		# messages = channel.message_set.all()
	# 	form = MessageForm(request.POST)
	# 	if form.is_valid():
	# 		new_message = form.save(commit=False)
	# 		new_message.profile=Profile.objects.get(user=request.user)
	# 		new_message.pub_date=datetime.now()
	# 		new_message.channel=channel_id
	# 		print(new_message)
	# 		new_message.save()
	# 		return redirect('index')
	# 		# return render(request, 'channeldetail.html', { 'channel': channel,'messages': messages, 'form': form})
	# else:
	# 	form = MessageForm()		
	# 	# return redirect('index')
	# 	return render(request, 'channeldetail.html', { 'channel': channel,'messages': messages, 'form': form})

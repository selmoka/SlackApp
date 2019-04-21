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

def userlist(request):
	profiles = Profile.objects.all()
	messages = Message.objects.all().select_related('profile_dest')
	return render(request, 'userlist.html',{
		'messages': messages,
		'profiles': profiles
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
	profile = Profile.objects.get(user=request.user)
	messages = channel.message_set.all().order_by('-pub_date')
	participants = channel.profile_part.all()
	return render(request, 'channeldetail.html', { 'channel': channel,
		'messages': messages, 'participants': participants})

def addmessage(request, channel_id): 
	channel = Channel.objects.get(pk=channel_id)
	messages = channel.message_set.all().order_by('-pub_date')
	if request.method == 'POST':
		message = Message()
		message.text = request.POST['text']
		try:
			img = request.FILES['img']
			fs = FileSystemStorage(location='media/images', base_url='/media/images')
			filename = fs.save(img.name, img)
			uploaded_file_url = fs.url(filename)
			message.img = uploaded_file_url
		except:
			pass
		message.profile = Profile.objects.get(user=request.user)
		message.channel = Channel.objects.get(pk=channel_id)
		message.pub_date = datetime.now()
		message.save()
	return render(request, 'channeldetail.html', { 'channel': channel,'messages': messages})

def addmessageuser(request, profile_id): 
	# channel = Channel.objects.get(pk=channel_id)
	# messages = channel.message_set.all().order_by('-pub_date')
	if request.method == 'POST':
		message = Message()
		message.text = request.POST['text']
		try:
			img = request.FILES['img']
			fs = FileSystemStorage(location='media/images', base_url='/media/images')
			filename = fs.save(img.name, img)
			uploaded_file_url = fs.url(filename)
			message.img = uploaded_file_url
		except:
			pass
		# user = User.objects.get(pk=user_id)
		profile_dest = Profile.objects.get(pk=profile_id)
		print(profile_dest)
		message.profile_dest = profile_dest
		message.profile = Profile.objects.get(user=request.user)
		print(message.profile)
		# message.channel = Channel.objects.get(pk=channel_id)
		message.pub_date = datetime.now()
		message.save()
		return render(request, 'userlist.html',{
		'users': User.objects.all().order_by('username'),
		'profiles': Profile.objects.all()
	}) 


def joinchannel(request, channel_id): 
	channel = Channel.objects.get(pk=channel_id)
	profile = Profile.objects.get(user=request.user)
	messages = channel.message_set.all().order_by('-pub_date')
	if request.method == 'POST':
		channel.profile_part.add(profile)
		channel.save()
		print(channel)
		participants = channel.profile_part.all()
		print('participants')
		print(participants)
		return render(request, 'channeldetail.html', { 'channel': channel,'messages': messages, 'participants': participants})
	return redirect('index')
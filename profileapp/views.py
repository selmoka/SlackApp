from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse, Http404
from .models import Profile
from slackapp.models import Channel, Message
from django.core.files.storage import FileSystemStorage
# from datetime import datetime

def profile(request):
	if request.user.is_authenticated:
		print(request.user)
		print(User)
		profile = Profile.objects.get(user=request.user)
		print(profile)
		return render(request, 'profile.html', {'profile': profile})
	else:
		return render(request, 'signin.html')

def addprofile(request):
	if request.user.is_authenticated:
		user = User.objects.get(username=request.user.username)
		if request.method == 'POST':
			if request.FILES['profile_pic']:
					profile_pic = request.FILES['profile_pic']
					profile_bio = request.POST['bio']
					fs = FileSystemStorage(location='media/images', base_url='/media/images')
					filename = fs.save(profile_pic.name, profile_pic)
					uploaded_file_url = fs.url(filename)
					pic = uploaded_file_url
					bio = profile_bio
					p = Profile(user=user, pic=pic, bio=bio)
					p.save()
					print(request.user)
					print(p)		
					return render(request, 'profile.html', {'profile': profile})
		else:
			return render(request, 'addprofile.html', {'profile': profile})

def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			# flash('This is error message', 'error')
			messages.add_message(request, messages.ERROR, 'Wrong user or password')
			return render(request, 'signin.html')
	return render(request, 'signin.html')

def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		bio = request.POST['bio']
		user = User.objects.create_user(username=username, password=password)
		if user is not None:
			user.save()
			profile = Profile(bio=bio, user=user)
			profile.save()
			login(request, user)
			return redirect('slack:index')
	return render(request, 'signup.html')

def signout(request):
	logout(request)
	return render(request, 'signin.html')

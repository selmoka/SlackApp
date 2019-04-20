from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse, Http404
from .models import Channel, Message
from profileapp.models import Profile
from datetime import datetime
from django.core.files.storage import FileSystemStorage


def index(request):
	return render(request, 'channels.html',{
		'channels': Channel.objects.all()
	}) 
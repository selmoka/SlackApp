import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Channel, Message

class ChannelForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text="Enter the channel title") 
    description = forms.CharField(widget=forms.Textarea, help_text="Enter the channel description")
    class Meta:
    	model = Channel
    	fields = ['title', 'description']

# class MessageForm(forms.ModelForm):
#     text = forms.CharField(help_text="Enter the message text") 
#     img = forms.FileField(help_text="Upload an image")
#     class Meta:
#     	model = Message
#     	fields = ['text', 'img']
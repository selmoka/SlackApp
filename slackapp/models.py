from django.db import models
from profileapp.models import Profile
from django.contrib.auth.models import User


class Channel(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	def __str__(self):
		return self.title

class Message(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published', default=None)
	text = models.TextField()
	img = models.ImageField(upload_to='media/images/', blank=True, null=True)
	def __str__(self):
	 	return self.profile.user.username + ' - ' + self.channel.title
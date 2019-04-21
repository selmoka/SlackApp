from django.db import models
from profileapp.models import Profile
from django.contrib.auth.models import User


class Channel(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	profile_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
	profile_part = models.ManyToManyField(Profile, related_name=
		'participants')
	# channel = models.ManyToManyField(Channel)
	def __str__(self):
		return self.title

class Message(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	profile_dest = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='destination', blank=True, null=True)
	channel = models.ForeignKey(Channel, on_delete=models.CASCADE, blank=True, null=True)
	pub_date = models.DateTimeField('date published', default=None)
	text = models.TextField()
	img = models.ImageField(upload_to='media/images/', blank=True, null=True)
	def __str__(self):
	 	return str(self.pub_date) + ' - ' + self.profile.user.username + ' - ' + self.text
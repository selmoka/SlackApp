from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	bio = models.TextField(default='', blank=True)
	pic = models.ImageField(upload_to='media/images/', blank=True, null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username
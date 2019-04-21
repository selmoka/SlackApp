from random import randint
from datetime import datetime
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'slack.settings')

import django
django.setup()

from slackapp.models import Channel, Message
from profileapp.models import Profile
from faker import Faker
from django.contrib.auth.models import User

if __name__ == '__main__':
	print('Starting to populate...')
	Profile.objects.all().delete()
	Message.objects.all().delete()
	Channel.objects.all().delete()

	fake = Faker()
	for _ in range(1,50):
		username = fake.user_name()
		password = fake.password()
		bio = fake.text()
		try:
			u = User.objects.create_user(username=username, password=password)
			print(u)
			u.save()
		except:
			pass

		try:
			p = Profile(bio=bio, user=u)
			p.save()
		except:
			pass

	for _ in range(1,50):
		title = fake.text()[0:99]
		description = fake.text()
		int = randint(0,20)
		print(int)
		profile = Profile.objects.all()[int]
		c = Channel(title=title, description=description, profile=profile)
		print(c)
		c.save()

	for _ in range(1,50):
		pub_date = datetime.now()
		text = fake.text()
		int = randint(0,49)
		profile = Profile.objects.all()[int]
		channel = Channel.objects.all()[int]
		m = Message(profile=profile, channel=channel, pub_date=pub_date, text=text)
		print(m)
		m.save()
		
	print('Finished populating!')
# Generated by Django 2.2 on 2019-04-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackapp', '0003_auto_20190421_1608'),
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='channel',
            field=models.ManyToManyField(to='slackapp.Channel'),
        ),
    ]
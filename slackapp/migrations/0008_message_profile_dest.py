# Generated by Django 2.2 on 2019-04-21 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0003_remove_profile_channel'),
        ('slackapp', '0007_auto_20190421_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='profile_dest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='profileapp.Profile'),
        ),
    ]

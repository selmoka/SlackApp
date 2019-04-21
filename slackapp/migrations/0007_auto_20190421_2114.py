# Generated by Django 2.2 on 2019-04-21 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0003_remove_profile_channel'),
        ('slackapp', '0006_auto_20190421_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='profile',
        ),
        migrations.AddField(
            model_name='channel',
            name='profile_owner',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='profileapp.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='channel',
            name='profile_part',
            field=models.ManyToManyField(related_name='participants', to='profileapp.Profile'),
        ),
    ]

# Generated by Django 4.2.16 on 2024-11-13 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_remove_event_thumbs_down_remove_event_thumbs_up_vote_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='thumbs_down',
        ),
        migrations.RemoveField(
            model_name='event',
            name='thumbs_up',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
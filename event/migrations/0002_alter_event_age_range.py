# Generated by Django 4.2.16 on 2024-11-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='age_range',
            field=models.CharField(choices=[(0, 'newborns'), (1, '0-12 months'), (2, '2-3 years'), (3, '4-5 years'), (4, '5-8 years'), (5, '8-12 years'), (6, '13+')], default=0),
        ),
    ]

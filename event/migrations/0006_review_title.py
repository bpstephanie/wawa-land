# Generated by Django 4.2.16 on 2024-11-11 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_review_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default='my_review', max_length=200),
        ),
    ]

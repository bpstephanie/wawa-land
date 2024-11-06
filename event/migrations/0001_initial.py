# Generated by Django 4.2.16 on 2024-11-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('event_about', models.TextField()),
                ('age_range', models.CharField(choices=[(1, '0-12 months'), (2, '2-3 years'), (3, '4-5 years'), (4, '5-8 years'), (5, '8-12 years'), (6, '13+')], default=1)),
                ('event_location', models.CharField(max_length=200, null=True)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('event_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('excerpt', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-event_date'],
            },
        ),
    ]

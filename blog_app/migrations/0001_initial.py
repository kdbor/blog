# Generated by Django 3.2.8 on 2021-10-26 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('cloud', 'Cloud'), ('space', 'Space'), ('ai', 'Ai')], default='space', max_length=50)),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('excerpt', models.CharField(max_length=150)),
                ('month', models.CharField(max_length=3)),
                ('day', models.CharField(max_length=2)),
                ('content', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2021, 10, 26, 21, 44, 10, 742479))),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-26 22:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_blogpost_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 22, 26, 11, 932338, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.2.9 on 2022-03-16 18:28

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_alter_blogpost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
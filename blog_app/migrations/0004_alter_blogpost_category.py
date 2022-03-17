# Generated by Django 3.2.9 on 2021-12-26 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('cloud', 'Cloud'), ('space', 'Space'), ('ai', 'Ai'), ('tech', 'Tech')], default='space', max_length=50),
        ),
    ]
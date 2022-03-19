# Generated by Django 4.0.3 on 2022-03-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0014_rename_thumbnail_src_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('Cloud', 'Cloud'), ('Space Sciences', 'Space'), ('Artificial Intelligence', 'Ai'), ('Opinion', 'Opinion'), ('Technology', 'Tech')], default='Space Sciences', max_length=50),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0018_remove_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.URLField(default='https://github.com/denniesbor/denniesbor.github.io/raw/assets/twist2/greg-jeanneau-9sxeKzuCVoE-unsplash.jpg'),
        ),
    ]

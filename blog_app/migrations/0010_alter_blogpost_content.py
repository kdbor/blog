# Generated by Django 3.2.9 on 2022-03-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_alter_blogpost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(),
        ),
    ]

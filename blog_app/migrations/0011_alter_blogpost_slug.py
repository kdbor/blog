# Generated by Django 3.2.9 on 2022-03-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0010_alter_blogpost_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="slug",
            field=models.SlugField(max_length=255),
        ),
    ]

# Generated by Django 3.2.9 on 2022-03-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0007_alter_blogpost_excerpt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="title",
            field=models.CharField(max_length=150),
        ),
    ]

# Generated by Django 3.2.9 on 2022-03-16 05:48

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_alter_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=django_quill.fields.QuillField(),
        ),
    ]

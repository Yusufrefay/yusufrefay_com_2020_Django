# Generated by Django 2.2.12 on 2021-04-19 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog',
            new_name='blog_post',
        ),
    ]
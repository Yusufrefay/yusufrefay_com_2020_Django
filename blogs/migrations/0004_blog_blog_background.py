# Generated by Django 3.1.4 on 2021-01-10 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20201219_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Blog_Background',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]

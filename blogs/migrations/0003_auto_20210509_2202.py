# Generated by Django 2.2.12 on 2021-05-09 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210509_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photographer',
            old_name='name',
            new_name='photographer_name',
        ),
        migrations.AlterField(
            model_name='blog',
            name='photographer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.Photographer'),
        ),
    ]

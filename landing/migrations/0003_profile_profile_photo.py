# Generated by Django 2.0.6 on 2018-06-27 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20180627_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.URLField(help_text='Link to avatar', null=True),
        ),
    ]
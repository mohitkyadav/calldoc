# Generated by Django 2.0.6 on 2018-06-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_remove_profile_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.URLField(null=True),
        ),
    ]
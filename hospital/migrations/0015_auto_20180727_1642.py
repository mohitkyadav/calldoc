# Generated by Django 2.0.5 on 2018-07-27 11:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0014_auto_20180727_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='email',
            field=models.EmailField(blank=True, help_text='Please enter valid email address, it will be used for verifications', max_length=254),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Please enter valid phone number', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:\\ '+919999999999'.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]

# Generated by Django 2.0.5 on 2018-07-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_auto_20180726_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]

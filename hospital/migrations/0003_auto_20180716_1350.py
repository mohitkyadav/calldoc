# Generated by Django 2.0.7 on 2018-07-16 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0012_auto_20180707_2150'),
        ('hospital', '0002_hospital_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='landing.City'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='landing.Region'),
        ),
    ]

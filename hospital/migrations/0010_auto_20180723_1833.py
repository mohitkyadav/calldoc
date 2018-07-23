# Generated by Django 2.0.6 on 2018-07-23 13:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0012_auto_20180707_2150'),
        ('hospital', '0009_hospital_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('patients_remarks', models.TextField(blank=True, null=True)),
                ('doctors_remarks', models.TextField(blank=True, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Doctor')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.Profile')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
                'ordering': ('-start_date',),
            },
        ),
        migrations.AlterField(
            model_name='hospital',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:\\ '+919999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]

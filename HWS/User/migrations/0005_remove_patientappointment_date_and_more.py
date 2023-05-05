# Generated by Django 4.2.1 on 2023-05-05 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_patientappointment_appointment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientappointment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='patientappointment',
            name='time',
        ),
        migrations.RemoveField(
            model_name='patientfeedback',
            name='x1',
        ),
        migrations.RemoveField(
            model_name='patientfeedback',
            name='x2',
        ),
        migrations.RemoveField(
            model_name='patientfeedback',
            name='x3',
        ),
        migrations.RemoveField(
            model_name='patientfeedback',
            name='x4',
        ),
        migrations.AddField(
            model_name='patientappointment',
            name='date_time',
            field=models.DateField(default=datetime.datetime(2023, 5, 5, 22, 42, 24, 465580)),
        ),
        migrations.AddField(
            model_name='patientfeedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 5, 22, 42, 24, 465580)),
        ),
        migrations.AddField(
            model_name='patientfeedback',
            name='description',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='patientfeedback',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
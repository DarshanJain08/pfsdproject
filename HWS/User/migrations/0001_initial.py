# Generated by Django 4.2.1 on 2023-05-05 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=20)),
                ('mail1', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=40)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('patientid', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=30)),
                ('secondname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='PatientFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('p_id', models.IntegerField()),
                ('phone', models.CharField(max_length=12)),
                ('doctor', models.CharField(max_length=30)),
                ('clinic', models.CharField(max_length=30)),
                ('x1', models.CharField(max_length=15)),
                ('x2', models.CharField(max_length=15)),
                ('x3', models.CharField(max_length=15)),
                ('x4', models.CharField(max_length=15)),
            ],
        ),
    ]
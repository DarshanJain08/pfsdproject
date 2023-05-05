# Generated by Django 4.2.1 on 2023-05-05 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=30)),
                ('secondname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=8)),
                ('role', models.CharField(default='patient', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='PatientDetails',
        ),
    ]
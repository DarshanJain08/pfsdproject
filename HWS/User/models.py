from django.db import models
import datetime

# Create your models here.
class PatientDetails(models.Model):
    patientid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=8)
    role=models.CharField(default="patient",max_length=10)

    def __str__(self):
        return self.firstname + " " + self.secondname
    
class DoctorDetails(models.Model):
    doctorid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=8)
    specializations=models.CharField(max_length=100)
    specialized_field=models.CharField(max_length=100)
    clinic_address = models.CharField(max_length=300)
    role=models.CharField(default="doctor",max_length=10)

    def __str__(self):
        return self.firstname + " " + self.secondname+" "+self.specialized_field

class PatientFeedback(models.Model):
    name = models.CharField(max_length=30)
    patientid = models.IntegerField()
    phone = models.CharField(max_length=12)
    doc_id = models.IntegerField(null=True)
    clinic = models.CharField(max_length=30)
    rating=models.IntegerField(default=0)
    description=models.TextField(max_length=300,null=True)
    date = models.DateField(default=datetime.datetime.now())

class PatientAppointment(models.Model):
    patient_id= models.IntegerField(null=True)
    doc_id = models.IntegerField(null=True)
    description = models.CharField(max_length=40)
    date_time = models.DateField(default=datetime.datetime.now())
    appointment_status=models.CharField(default="accepted",max_length=40)
# Create your models here.

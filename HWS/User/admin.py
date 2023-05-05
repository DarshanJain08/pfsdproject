from django.contrib import admin
from .models import *

admin.site.register(PatientDetails)
admin.site.register(DoctorDetails)
admin.site.register(PatientAppointment)
admin.site.register(PatientFeedback)

# Register your models here.

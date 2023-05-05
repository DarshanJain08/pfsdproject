from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import *
from django.core.mail import send_mail
import math, random

def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def doc_home(request):
    return render(request,"doc_home_page.html")

def pat_home(request):
    return render(request,"pat_home_page.html")

def logined(request):
    if request.method=="POST":
        uname=request.POST['email']
        psw=request.POST['password']
        data1=PatientDetails.objects.filter(email=uname, password=psw)
        if data1 :
            return redirect('pat_home')
        else:
            data2=DoctorDetails.objects.filter(email=uname, password=psw)
            if data2 :
                return redirect('doc_home')
    else:
        return render(request,"signup.html")

def doc_signup(request):
    return render(request,"doc_signup.html")


def pat_signup(request):
    return render(request,"pat_signup.html")

def doc_signuped(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        password=request.POST['password']
        gender=request.POST['gender']
        specializations=request.POST['specializations']
        field=request.POST['field']
        address=request.POST['address']
        d=DoctorDetails.objects.create()
        d.firstname=firstname
        d.secondname=lastname
        d.phone=phoneno
        d.email=email
        d.password=password
        d.gender=gender
        d.specializations=specializations
        d.specialized_field=field
        d.clinic_address=address
        d.save()
        return redirect('login')
    

def logout(request):
    return redirect('')

def pat_signuped(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        password=request.POST['password']
        gender=request.POST['gender']
        pd=PatientDetails.objects.create()
        pd.firstname=firstname
        pd.secondname=lastname
        pd.phone=phoneno
        pd.email=email
        pd.password=password
        pd.gender=gender
        pd.save()
        return redirect('login')

def feedback(request):
    if request.method=="POST":
        name=request.POST['name']
        p_id=int(request.POST['p_id'])
        phone=request.POST['phone']
        doctor=request.POST['doctor']
        clinic=request.POST['clinic']
        x1=request.POST['x1']
        x2=request.POST['x2']
        x3=request.POST['x3']
        x4=request.POST['x4']
        data2=PatientFeedback(name=name, p_id=p_id,phone=phone,doctor=doctor,clinic=clinic,x1=x1,x2=x2,x3=x3,x4=x4)
        data2.save()
        return HttpResponse("Feedback Saved")
    else:
        return render(request,"feedback.html")

def doctors(request):
    return render(request,"doctors.html")

def appointments(request):
    if request.method=="POST":
        name1=request.POST['name1']
        mail1=request.POST['mail1']
        telephone=request.POST['telephone']
        description=request.POST['description']
        date=request.POST['date']
        time=request.POST['time']
        data3=PatientAppointment(name1=name1,mail1=mail1,telephone=telephone,description=description,date=date,time=time)
        data3.save()
        return HttpResponse("Appointment booked")
    else:
        return render(request,"appointments.html")



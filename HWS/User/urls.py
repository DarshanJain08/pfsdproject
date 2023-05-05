from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('doctors',views.doctors, name='doctors'),
    path('appointments',views.appointments, name='appointments'),
    path('feedback',views.feedback, name='feedback'),
    path('login',views.login, name='login'),
    path('logined',views.logined, name='logined'),
    path('logout',views.logout, name='logout'),
    path('docsignup',views.doc_signup, name='docsignup'),
    path('docsignuped',views.doc_signuped, name='docsignuped'),
    path('patsignup',views.pat_signup, name='patsignup'),
    path('patsignuped',views.pat_signuped, name='patsignuped'),
    path('pat_home',views.pat_home, name='pat_home'),
    path('doc_home',views.doc_home, name='doc_home'),
]
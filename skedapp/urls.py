from skedapp.models import register
from django.contrib import admin
from django.urls import path
from .views import deleteevents, studlist,userlogout,customerwelcomeview,signupuser,homepageview,deleteevent,addevent, adminhomepageview, adminloginview, authenticateadmin, logoutadmin, userauthentication, userloginview,reg

urlpatterns = [
    path('admin/',adminloginview,name = 'adminloginpage'),
    path('adminauthenticate/',authenticateadmin),
    path('admin/homepage/',adminhomepageview,name = 'adminhomepage'),
    path('adminlogout/',logoutadmin),
    path('addevent/',addevent),
    path('deleteevent/<int:eventpk>/',deleteevent),
    path('',homepageview,name = 'homepage'),
    path('signupuser/',signupuser),
    path('loginuser/',userloginview,name = 'userloginpage'),
    path('customer/welcome/',customerwelcomeview,name = 'customerpage'),
    path('customer/authenticate/',userauthentication),
    path('userlogout/',userlogout),
    path('reg/',reg),
    path('studlist/',studlist,name = 'studlist'),
    path('deleteevents/<int:eventpk>/',deleteevents)
]

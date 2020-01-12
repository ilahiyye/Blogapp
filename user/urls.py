"""ARTICLA AID OLAN URLLARI BURA YAZIRIQ"""
from django.contrib import admin
from django.urls import path
from . import views             #bu papqanin(.) icindeki views faylini import edir

app_name = 'USER'               #tetbiqe ad veririk

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.loginUser, name='login'),
    path('logout/',views.logoutUser, name='logout'),
]
"""ARTICLA AID OLAN URLLARI BURA YAZIRIQ"""
from django.contrib import admin
from django.urls import path
from . import views                          #bu papqanin(.) icindeki views faylini import edir
  



app_name = 'article'            #tetbiqe ad veririk

urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('addarticle/', views.addArticle, name='addarticle'),
    path('update/<int:id>', views.updateArticle, name='update'),
    path('delete/<int:id>', views.deleteArticle, name='delete'),
    path('comment/<int:id>', views.addComment, name='comment'),


]


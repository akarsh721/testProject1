from os import name
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('updateProfile/<int:id>',views.updateProfile,name="updateProfile"),
    path('fetchqueries/',views.fetchqueries,name="fetchqueries"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('contact/writeUs/',views.writeUs,name="contact_writeUs"),
]
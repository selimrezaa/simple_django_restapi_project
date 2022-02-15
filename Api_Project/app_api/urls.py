from django.contrib import admin
from django.urls import path
from app_api import views

app_name = 'app_api'
urlpatterns = [
    path('', views.index),
    path('student/', views.student),
    path('student/<pk>', views.single_student),
    path('msg/<pk>', views.whatsapp_msg, name='msg'),
]

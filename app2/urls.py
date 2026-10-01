from django.contrib import admin
from django.urls import path
from . import views

app_name="app1"

urlpatterns = [
    path('vista1/', views.vista1,name='v1'),
]
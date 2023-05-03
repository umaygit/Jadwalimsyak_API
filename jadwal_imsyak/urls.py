from django.urls import path
from . import views

app_name = 'jadwal_Imsyak1444_Lotim'

urlpatterns = [
    path('', views. readjadwal),
    path('buat/', views. createjadwal)
]
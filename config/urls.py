# config/urls.py
from django.contrib import admin
from django.urls import path, include
from chart import views                                     # !!!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('covid/', views.covid, name='covid'),
    path('recovered/', views.recovered, name='recovered'),
    path('deaths/', views.deaths, name='deaths'),
]
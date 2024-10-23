from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('adminDashboard',views.adminDashboard,name='admindashboard'),
    path('login',views.adminLogin,name='adminLogin'),
]
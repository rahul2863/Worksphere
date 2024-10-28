from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    #add blank_path in jobseeker.urls
    path('seekerDashboard',views.seekerDashboard,name='seekerdashboard'),
    path('login',views.seekerLogin,name='seekerLogin'),
    path('register',views.seekerRegister,name='register'),


    #Common functionalities for all
    path('',views.homePage,name='home'),
    path('about',views.aboutPage,name='about'),
    path('contact',views.contactPage,name='contact')
    
]

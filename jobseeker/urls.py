from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    #add blank_path in jobseeker.urls
    path('',views.homePage,name='home'),
    path('seekerDashboard',views.seekerDashboard,name='seekerdashboard'),
    path('login',views.seekerLogin,name='seekerLogin'),
]
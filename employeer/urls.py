from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    #add blank_path in jobseeker.urls
    path('empDashboard',views.empDashboard,name='empdashboard'),
    path('login',views.empLogin,name='login'),
    path('register',views.empRegister,name='register'),
    path('postJob',views.postJob,name='postJob'),
]
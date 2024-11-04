from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    #add blank_path in jobseeker.urls
    path('ShowJobByCategory/<int:id>/',views.showJob, name='ShowJobByCategory'),
    path('job-list',views.jobList,name='JobList'),
    path('job-detail',views.jobDetail,name='JobList'),
    #Common functionalities for all
    path('',views.homePage,name='home'),
    path('about',views.aboutPage,name='about'),
    path('contact',views.contactPage,name='contact'),
    path('login',views.commonLogin,name='login'),
    path('register',views.commonRegister,name='register'),
    path('logout',views.commonLogout,name='logout'),
    path('forgot_password',views.forgotPassword,name='forgot_password'),
]

from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    #add blank_path in jobseeker.urls
    path('empProfile',views.empProfile,name='empProfile'),
    path('postJob',views.postJob,name='postJob'),
]
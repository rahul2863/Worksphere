from django.shortcuts import render
from common_tables.models import Users,Skills,Employeers,Jobs,JobRequirements,JobApplications,JobSeeker,JobSeekerSkills,SavedJobs
# Create your views here.
def homePage(request):
    return render(request,'jobseeker/home.html',{'title':'Home Page'})

def seekerLogin(request):
    if request.method == 'GET':
        return render(request,'jobseeker/seekerLogin.html',{'title':'Seeker Login'})
    else:
        pass

def seekerRegister(request):
    if request.method == "GET":
        return render(request,'jobseeker/seekerRegister.html',{'title':'Seeker Register'})
    else:
        pass
    
def seekerDashboard(request):
    return render(request,'jobseeker/seekerdashboard.html',{'title':'Seeker Dashboard'})
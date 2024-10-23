from django.shortcuts import render
from common_tables.models import Users,Skills,Employeers,Jobs,JobRequirements,JobApplications,JobSeeker,JobSeekerSkills,SavedJobs
# Create your views here.
def homePage(requests):
    return render(requests,'jobseeker/home.html',{'title':'Home Page'})

def seekerLogin(requests):
    if requests.method == 'GET':
        return render(requests,'jobseeker/seekerLogin.html',{'title':'Seeker Login'})
    else:
        pass

def seekerDashboard(requests):
    return render(requests,'jobseeker/seekerdashboard.html',{'title':'Seeker Dashboard'})
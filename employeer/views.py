from django.shortcuts import render
from common_tables.models import Users,Skills,Employeers,Jobs,JobRequirements,JobApplications,JobSeeker,JobSeekerSkills,SavedJobs
# Create your views here.
def empDashboard(requests):
    return render(requests,'employeer/empdashboard.html',{'title':'Employeer Dashboard'})


def empLogin(requests):
    if requests.method == 'GET':
        return render(requests,'employeer/empLogin.html',{'title':'Employeer Login'})
    else:
        pass
from django.shortcuts import render,redirect
from jobseeker.models import User,JobSeekerProfile,JobSeekerSkills,SavedJobs,Skill
from employeer.models import EmployerProfile,JobApplications,JobRequirement,Job
from django.http import HttpResponse
# Create your views here.
def empDashboard(request):
    return render(request,'employeer/empdashboard.html',{'title':'Employeer Dashboard'})

def postJob(request):
    if 'user' in request.session:
        return render(request,'employeer/postjob.html')
    else:
        return redirect('/jobseeker/login')
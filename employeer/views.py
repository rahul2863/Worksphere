from django.shortcuts import render
from jobseeker.models import User,JobSeekerProfile,JobSeekerSkills,SavedJobs,Skill
from employeer.models import EmployerProfile,JobApplications,JobRequirement,Job
from django.http import HttpResponse
# Create your views here.
def empDashboard(request):
    return render(request,'employeer/empdashboard.html',{'title':'Employeer Dashboard'})


def empLogin(request):
    if request.method == 'GET':
        return render(request,'employeer/empLogin.html',{'title':'Employeer Login'})
    else:
        pass

def empRegister(request):
    if request.method == 'GET':
        return render(request,'employeer/empRegister.html',{'title':'Employeer Register'})
    else:
        # return HttpResponse("Register Success")
        email = request.POST.get('email')
        print(email)
        name = request.POST.get('username')
        print(name)
        password = request.POST.get('password')
        print(password)
        return render(request,'employeer/sample.html',{'name':name,'email':email,'password':password})

def newFunc(request):
    pass
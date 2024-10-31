from django.shortcuts import render,redirect
from jobseeker.models import User,JobSeekerProfile,JobSeekerSkills,SavedJobs,Skill
from employeer.models import EmployerProfile,JobApplications,JobRequirement,Job
from django.http import HttpResponse
from .forms import JobPostForm
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

def postJob(request):
    if request.method == "GET":
        form = JobPostForm()
        return render(request,'employeer/JobPost.html',{'form':form})
    else:
        form = JobPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jobseeker:home')
    # return render(request,'employeer/postJob.html')
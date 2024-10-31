from django.shortcuts import render,redirect
from jobseeker.models import User,JobSeekerProfile,JobSeekerSkills,SavedJobs,Skill
from employeer.models import EmployerProfile,JobApplications,JobRequirement,Job
from django.http import HttpResponse
from .forms import JobPostForm, RegisterForm
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
        registerForm = RegisterForm()
        return render(request,'employeer/empRegister.html',{'title':'Employeer Register','form':registerForm})
    else:
        try:
            form = RegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/employeer/empLogin')
        except:
            return HttpResponse('Invalid Data')

def postJob(request):
    if 'user' in request.session:
        if request.method == "GET":
            form = JobPostForm()
            return render(request,'employeer/JobPost.html',{'form':form})
        else:
            form = JobPostForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                #redirecting to the link which is present in another app(jobseeker app)
                return redirect('jobseeker:home')
    else:
        # return HttpResponse("Login or register first")
        return redirect('/employeer/empLogin')
    # return render(request,'employeer/postJob.html')
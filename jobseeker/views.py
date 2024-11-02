from django.shortcuts import render,redirect
from jobseeker.models import User,JobSeekerProfile,JobSeekerSkills,SavedJobs,Skill
from employeer.models import EmployerProfile,JobApplications,JobRequirement,Job
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth import authenticate, login
import json

# Create your views here.
def homePage(request):
    return render(request,'home.html')

def aboutPage(request):
    return render(request,'about.html')

def contactPage(request):
    return render(request,'contact.html')


def commonLogin(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        # Collect the username and password from the form
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            return redirect(commonRegister)
        else:
            if check_password(password,user.password):
                request.session['user'] = user.name
                return render(request,'home.html',{'role':user.role})
            else:
                return redirect(commonLogin)


def commonRegister(request):
    if request.method == "GET":
        return render(request,'register.html')
    elif request.method == "POST":
        # Collect data from the form
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")
        phone = request.POST.get("phone")
        profile_image = request.FILES.get("profile_image")
        address = request.POST.get("address")

        # Validate data (you may want more comprehensive validation here)
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect(commonRegister)
        
        user = User(
            name = name,
            email=email,
            password=make_password(password),  # Hash the password
            phone_number = phone,
            profile_image = profile_image,
            address = address,
            role = role,
        )

        user.save()
        messages.success(request, "Account created successfully. You can now log in.")
        return redirect('login')
        
    
def seekerDashboard(request):
    return render(request,'jobseeker/seekerdashboard.html',{'title':'Seeker Dashboard'})
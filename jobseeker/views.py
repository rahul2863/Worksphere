from django.shortcuts import render,redirect
from django.http import HttpResponse
from jobseeker.models import User,JobSeekerProfile,JobSeekerSkills,SavedJobs,Skill
from employeer.models import EmployerProfile,JobApplications,JobRequirement,Job,JobCategory
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
            print(user.role,user.name)
        except:
            return redirect(commonRegister)
        else:
            if check_password(password,user.password):
                request.session['user'] = user.name
                request.session['user_role'] = user.role
                return render(request,'home.html',{'user_name':user.name,'role':user.role})
            else:
                return redirect(commonLogin)

def commonLogout(request):
    if 'user' in request.session:
        request.session.flush()
        return redirect('home')
    
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

def forgotPassword(request):
    if request.method == 'GET':
        return render(request,'forgot_password.html') 
    else:
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if not email or not pass1 or not pass2:
            return render(request, 'forgot_password.html', {'message': 'All fields are required!'})

        if pass1 != pass2:
            return render(request, 'forgot_password.html', {'message': 'Passwords do not match!'})


        #User.DoesNotExist is an inbuilt exception in Django that is raised when a User object cannot be found in the database.
        # Explanation:
        # When you use User.objects.get(email=email), Django attempts to find a user with the given email.
        # If no matching record is found, Django raises a DoesNotExist exception specific to the User model class.
        # DoesNotExist exception can be raised for others model as well ,in this case we are finding user with email hence User Model.

        try:
            user = User.objects.get(email=email)
            user.password = make_password(pass1)  # This properly hashes the password
            user.save()  # Save the changes to the database
            return render(request, 'forgot_password.html', {'message': 'Password Reset Success!!'})
        except User.DoesNotExist:
            return render(request, 'forgot_password.html', {'message': 'Please Enter a Valid Email!!'})
        except Exception as e:
            # Log the exception if necessary
            print(e)
            return render(request, 'forgot_password.html', {'message': 'An error occurred. Please try again later.'})

def jobList(request):
        return render(request,'job-list.html')

def jobDetail(request):
        return render(request,'job-detail.html')

def showJob(request, id=id):
    job_category = JobCategory.objects.get(category_id = id)
    jobs = Job.objects.filter(category = job_category)
    return render(request,'job-list.html',{'jobs':jobs})
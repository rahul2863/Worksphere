from django.shortcuts import render,redirect
from jobseeker.models import User,JobSeekerProfile,JobSeekerSkills,SavedJobs,Skill
from employeer.models import EmployerProfile,JobApplications,JobRequirement,Job,JobCategory
from django.http import HttpResponse
# Create your views here.
def empProfile(request):
    if request.method == 'GET':
        user = User.objects.get(name=request.session['user'])
        if user.profile_complete:
            return render(request,'view_profile.html',{'message':'Profile is Complete'})
        else:
            return render(request,'view_profile.html',{'message':'Complete Your Profile'})
    else:
        user = User.objects.get(name=request.session['user'])
        employer = user

        companyname = request.POST.get('companyname')
        website = request.POST.get('website')
        industry = request.POST.get('industry')
        companysize = request.POST.get('companysize')
        logo = request.FILES.get('logo')
        contactperson = request.POST.get('contactperson')
        phonenumber = request.POST.get('phonenumber')
        address = request.POST.get('address')

        emp = EmployerProfile(employer=employer,company_name=companyname,company_website = website, industry = industry, 
                              company_size = companysize, company_address=address, logo=logo,
                              contact_person = contactperson, phone_number = phonenumber)
        emp.save()
        
        #Marking profile as complete in User table
        user = User.objects.get(name=request.session['user'])
        user.profile_complete = 1
        user.save()
        return render(request,'view_profile.html',{'message':'Profile Complete'})
    
def postJob(request):
    if request.method == 'GET':
        if 'user' in request.session:
            #if profile complete then only allow recruiter to post a job
            print(request.session['user'])
            user = User.objects.get(name = request.session['user'])
            if user.profile_complete:
                #employers, categories taken to display in postjob form
                employers = EmployerProfile.objects.all()
                categories = JobCategory.objects.all()
                return render(request,'employeer/postjob.html',{'categories':categories,'employers':employers})
            else:
                return render(request,'view_profile.html',{'message':'Complete your profile to post a job'})
        else:
            return redirect('/jobseeker/login')
    else:
        job_title = request.POST.get('jobTitle')
        company = request.POST.get('company')
        job_res = request.POST.get('jobResponsibilityContent')
        qualifications = request.POST.get('qualificationsContent')
        category = request.POST.get('jobCategory')
        salary_from = request.POST.get('salaryFrom')
        salary_to = request.POST.get('salaryTo')
        vacancy = request.POST.get('vacancy')
        location = request.POST.get('location')
        jobType = (request.POST.get('jobType'))

        employer = EmployerProfile.objects.get(company_name=company)
        category = JobCategory.objects.get(name = category)

        job = Job(job_title=job_title, employer = employer, job_description = job_res, 
                  qualifications = qualifications, category = category, salary_from = salary_from, 
                  salary_to = salary_to, vacancy = vacancy, job_type = jobType, location=location)
        job.save()
        return redirect('home')
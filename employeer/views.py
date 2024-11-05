from django.shortcuts import render,redirect
from jobseeker.models import User,JobSeekerProfile,JobSeekerSkills,SavedJobs,Skill
from employeer.models import EmployerProfile,JobApplications,JobRequirement,Job,JobCategory
from django.http import HttpResponse
# Create your views here.
def empDashboard(request):
    return render(request,'employeer/empdashboard.html',{'title':'Employeer Dashboard'})

def postJob(request):
    if request.method == 'GET':
        if 'user' in request.session:
            employers = EmployerProfile.objects.all()
            categories = JobCategory.objects.all()
            return render(request,'employeer/postjob.html',{'categories':categories,'employers':employers})
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
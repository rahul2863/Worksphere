from django.db import models
from jobseeker.models import User  # Import from JobSeeker app

class EmployerProfile(models.Model):
    employer = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=100)
    company_website = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=100)
    company_size = models.IntegerField()
    company_address = models.CharField(max_length=255)
    logo = models.URLField(blank=True, null=True)
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "emp_profile"

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, default=1)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    qualifications = models.TextField(default="Screw Qualifications but can you cook?")
    vacancy = models.IntegerField(default=0)
    
    # Salary range fields
    salary_from = models.BigIntegerField()
    salary_to = models.BigIntegerField()
    
    location = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)
    
    # Job type and status
    job_type = models.CharField(max_length=20, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Remote', 'Remote'), ('Contract', 'Contract')])
    status = models.CharField(max_length=10, choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open')
    
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "job"

    
class JobApplications(models.Model):
    application_id = models.AutoField(primary_key=True)
    seeker = models.ForeignKey('jobseeker.JobSeekerProfile', on_delete=models.CASCADE)  # Foreign key to JobSeekerProfile
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    #status ENUM(data type in sql)
    status = models.CharField(max_length=15, choices=[('Applied', 'Applied'), ('Shortlisted', 'Shortlisted'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')], default='Applied')
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "job_applications"


class JobRequirement(models.Model):
    requirement_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    required_skill = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "job_requirement"


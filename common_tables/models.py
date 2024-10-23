from django.db import models

# Create your models here.
class Users(models.Model):
    USER_ROLE = 'User'
    ADMIN_ROLE = 'Admin'
    EMPLOYEER_ROLE = 'Employeer'

    ROLE_CHOICES = [
        (USER_ROLE, 'User'),
        (ADMIN_ROLE, 'Admin'),
        (EMPLOYEER_ROLE ,'Employeer')
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=USER_ROLE)
    phn_no = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    address = models.TextField()
    profile_complete = models.BooleanField()
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Users'

    def __str__(self):
        return f"{self.name}"
    

class Skills(models.Model):
    skill_name = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "Skills"



## Employeers table
class Employeers(models.Model):
    company_name = models.CharField(max_length=255)
    company_website = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    company_size = models.IntegerField()
    company_address = models.TextField()
    logo = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phn_no = models.CharField(max_length=10)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "Employeers"


class Jobs(models.Model):
    JOB_TYPES = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Hybrid', 'Hybrid'),
        ('Remote', 'Remote'),  # You can add more statuses if needed
    ]

    STATUS = [
        ('Open','Open'),
        ('Closed','Closed'),
    ]

    employer_id = models.ForeignKey(Employeers,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default='Full-Time')
    salary_range = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS, default='Open')
    deleted = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Jobs'


class JobRequirements(models.Model):
    job_id = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    required_skills = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "JobRequirements"


## Jobs Table
class JobSeeker(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Looking', 'Looking'),
        ('Not Looking', 'Not Looking'),
        ('Closed', 'Closed'),  # You can add more statuses if needed
    ]

    seeker_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    resume = models.CharField(max_length=255)
    skills = models.TextField()
    experience_years = models.IntegerField()
    education = models.TextField()
    expected_salary = models.CharField(max_length=255)
    location_preference = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Looking')
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'JobSeeker'


class JobSeekerSkills(models.Model):
    seeker_id = models.ForeignKey(JobSeeker,on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skills,on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'jobseekerskills'


class SavedJobs(models.Model):
    seeker_id = models.ForeignKey(JobSeeker,on_delete=models.CASCADE)
    job_id = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "SavedJobs"





class JobApplications(models.Model):
    STATUS = [
        ('Applied','Applied'),
        ('Shortlisted','Shortlisted'),
        ('Rejected','Rejected'),
        ('Accepted','Accepted'),
    ]

    seeker_id = models.ForeignKey(JobSeeker,on_delete=models.CASCADE)
    job_id = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255,choices=STATUS,default='Applied')
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "JobApplications"
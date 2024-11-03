from django.db import models
class User(models.Model):
    ROLE_CHOICES = [
        ('Job Seeker', 'Job Seeker'),
        ('Employer', 'Employer'),
        ('Admin', 'Admin')
    ]
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to='Images/',default='abc.jpg')
    address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_complete = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "user" 

    def __str__(self):
        return self.name

class JobSeekerProfile(models.Model):
    seeker = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    resume = models.URLField()
    skills = models.TextField()
    experience_years = models.IntegerField()
    education = models.TextField()
    expected_salary = models.CharField(max_length=50)
    location_preference = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Looking', 'Looking')], default='Looking')
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "job_seeker_profile"
    

class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "skill"
    
    def __str__(self):
        return self.skill_name

class JobSeekerSkills(models.Model):
    seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "job_seeker_skills"


class SavedJobs(models.Model):
    saved_job_id = models.AutoField(primary_key=True)
    seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    job = models.ForeignKey('employeer.Job', on_delete=models.CASCADE)  # Foreign key to Employer app's Job model
    saved_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "saved_jobs"

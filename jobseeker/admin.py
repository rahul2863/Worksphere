from django.contrib import admin
from jobseeker.models import JobSeekerProfile,JobSeekerSkills,SavedJobs,Skill,User
# Register your models here.

class JobSeekerProfileAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in JobSeekerProfile._meta.fields]

class JobSeekerSkillsAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in JobSeekerSkills._meta.fields]

class SavedJobsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SavedJobs._meta.fields]

class SkillAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Skill._meta.fields]

class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]


admin.site.register(JobSeekerProfile,JobSeekerProfileAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(SavedJobs,SavedJobsAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(JobSeekerSkills,JobSeekerSkillsAdmin)
from django.contrib import admin
from employeer.models import Job,JobCategory,JobApplications,JobRequirement,EmployerProfile
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Job._meta.fields]

class JobApplicationsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in JobApplications._meta.fields]

class JobRequirementAdmin(admin.ModelAdmin):
    list_display = [field.name for field in JobRequirement._meta.fields]

class JobCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in JobCategory._meta.fields]

class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EmployerProfile._meta.fields]


admin.site.register(Job, JobAdmin)
admin.site.register(JobApplications, JobApplicationsAdmin)
admin.site.register(JobRequirement, JobRequirementAdmin)
admin.site.register(JobCategory, JobCategoryAdmin)
admin.site.register(EmployerProfile, EmployerProfileAdmin)




from django import forms
from .models import Job,User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'job_title', 'job_description', 'qualifications',
            'salary_from','salary_to', 'vacancy', 'location', 'job_type'
        ]

    def __init__(self,*args,**kwargs):
        super(JobPostForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'job-post-form'  # Add custom form class if needed
        self.helper.add_input(Submit('submit', 'Post Job', css_class="btn-primary mt-4 px-5"))

         # Add placeholder and class for each field
        self.fields['job_title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Job Title'})
        self.fields['job_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Describe job responsibilities'})
        self.fields['qualifications'].widget.attrs.update({'class': 'form-control', 'placeholder': 'List required qualifications'})
        self.fields['salary_from'].widget.attrs.update({'class': 'form-control', 'placeholder': 'From Salary'})
        self.fields['salary_to'].widget.attrs.update({'class': 'form-control', 'placeholder': 'To Salary'})
        self.fields['vacancy'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Number of positions available'})
        self.fields['location'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Job location'})
        self.fields['job_type'].widget.attrs.update({'class': 'form-control'})


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'name', 'email', 'password',
            'role','phone_number', 'profile_image', 'address'
        ]

    def __init__(self,*args,**kwargs):
        super(RegisterForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'user-register'  # Add custom form class if needed
        self.helper.add_input(Submit('submit', 'Register', css_class="btn-primary mt-4 px-5"))

        # Add placeholder and class for each field
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['role'].widget.attrs.update({'class': 'form-control', 'placeholder': 'role'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'phone number'})
        self.fields['profile_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'address'})

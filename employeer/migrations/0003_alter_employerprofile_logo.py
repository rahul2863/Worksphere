# Generated by Django 5.1.1 on 2024-11-03 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeer', '0002_jobcategory_job_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employerprofile',
            name='logo',
            field=models.ImageField(default='company.jpg', upload_to='Images/company'),
        ),
    ]

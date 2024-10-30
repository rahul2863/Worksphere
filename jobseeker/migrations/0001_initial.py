# Generated by Django 5.1.1 on 2024-10-28 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('Job Seeker', 'Job Seeker'), ('Employer', 'Employer'), ('Admin', 'Admin')], max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('profile_image', models.URLField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile_complete', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='JobSeekerSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'job_seeker_skills',
            },
        ),
        migrations.CreateModel(
            name='SavedJobs',
            fields=[
                ('saved_job_id', models.AutoField(primary_key=True, serialize=False)),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'saved_jobs',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill_id', models.AutoField(primary_key=True, serialize=False)),
                ('skill_name', models.CharField(max_length=100)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'skill',
            },
        ),
        migrations.CreateModel(
            name='JobSeekerProfile',
            fields=[
                ('seeker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='jobseeker.user')),
                ('resume', models.URLField()),
                ('skills', models.TextField()),
                ('experience_years', models.IntegerField()),
                ('education', models.TextField()),
                ('expected_salary', models.CharField(max_length=50)),
                ('location_preference', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Looking', 'Looking')], default='Looking', max_length=20)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'job_seeker_profile',
            },
        ),
    ]
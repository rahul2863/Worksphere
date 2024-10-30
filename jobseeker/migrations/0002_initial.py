# Generated by Django 5.1.1 on 2024-10-28 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employeer', '0001_initial'),
        ('jobseeker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedjobs',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeer.job'),
        ),
        migrations.AddField(
            model_name='jobseekerskills',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseeker.skill'),
        ),
        migrations.AddField(
            model_name='savedjobs',
            name='seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseeker.jobseekerprofile'),
        ),
        migrations.AddField(
            model_name='jobseekerskills',
            name='seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseeker.jobseekerprofile'),
        ),
    ]
# Generated by Django 5.1.1 on 2024-10-31 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeer', '0004_alter_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='employer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employeer.employerprofile'),
        ),
    ]

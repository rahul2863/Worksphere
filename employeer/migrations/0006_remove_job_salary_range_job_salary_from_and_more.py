# Generated by Django 5.1.1 on 2024-10-31 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeer', '0005_alter_job_employer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='salary_range',
        ),
        migrations.AddField(
            model_name='job',
            name='salary_from',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='salary_to',
            field=models.BigIntegerField(default=0),
        ),
    ]

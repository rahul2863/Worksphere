# Generated by Django 5.1.1 on 2024-11-04 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employerprofile',
            name='logo',
            field=models.ImageField(default='company.jpg', upload_to='Images/company/'),
        ),
    ]
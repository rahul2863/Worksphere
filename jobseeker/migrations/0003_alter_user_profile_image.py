# Generated by Django 5.1.1 on 2024-10-31 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='abc.jpg', upload_to='Images/'),
        ),
    ]

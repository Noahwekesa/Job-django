from django.db import models
from users.models import User
from django.core.validators import RegexValidator

# Create your models here.

GENDER_CHOICES = [
     ('null', 'not specified'),
    ('Male', 'Male'),
     ('Female', 'Female'),
]
class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    bio = models.TextField(null=True, blank=True)
    skills = models.TextField(blank=True, null=True)
    experience =models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='null')
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='resume/', default='Default.jpg')
    cv = models.FileField(upload_to='resume', null=True, blank=True)
    

    def __str__(self):
        return f'{self.firstname} {self.surname}'


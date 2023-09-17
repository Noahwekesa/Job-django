from django.db import models

GENDER_MALE = 'male'
GENDER_FEMALE = 'Female'
GENDER_CHOICES = (
    (GENDER_MALE,  'male'),
    (GENDER_FEMALE, 'female')
    )
# Create your models here.
class JobSeeker(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    skills = models.TextField()
    experience = models.IntegerField()
    education = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resumes')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=GENDER_MALE)

    def __str__(self):
        return self.full_name
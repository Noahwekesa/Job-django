from django.db import models


GENDER_MALE = 'male'
GENDER_FEMALE = 'Female'
GENDER_CHOICES = (
    (GENDER_MALE,  'male'),
    (GENDER_FEMALE, 'female')
    )

STATUS_PENDING = 'pending'
STATUS_APPROVED = 'approved'
STATUS_REJECTED = 'rejected'
STATUS_CHOICES = (
    (STATUS_PENDING, 'pending'),
    (STATUS_APPROVED, 'approved'),
    (STATUS_REJECTED, 'rejected')
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
    
class Jobseekerjobmap(models.Model):
   JobSeeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
   job = models.ForeignKey('job.job', on_delete=models.CASCADE)
   status = models.CharField(max_length=20, choices=STATUS_CHOICES,  default=STATUS_PENDING)
   feedback = models.TextField(blank=True, null=True)
   
   
   def __str__(self):
      return"{} - {}".format(self.JobSeeker.full_name, self.job.title)
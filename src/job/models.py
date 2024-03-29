from django.db import models
from job.consts import INDUSTRY, LOCATION
from users.models import User
from company.models import Company


class Job(models.Model):
    job_type_choices = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Remote', 'Remote'),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    salary = models.IntegerField(default=35000)
    requirements = models.TextField()
    ideal_candidate = models.TextField()
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    industry = models.CharField(
        max_length=24,
        choices=INDUSTRY,
        null=True,
        blank=True)

    city = models.CharField(
        max_length=24,
        choices=LOCATION,
        null=True,
        blank=True
    )
    job_type = models.CharField(
        max_length=100, choices=job_type_choices, null=True, blank=True)

    def __str__(self):
        return self.title


class ApplyJob(models.Model):
    JOB_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job,     on_delete=models.CASCADE)
    content = models.CharField(max_length=20000, null=True, blank=True, )
    experience = models.PositiveBigIntegerField(null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    job_status = models.CharField(
        max_length=20, choices=JOB_STATUS_CHOICES, default='Pending')


class ConversationMessage(models.Model):
    applyjob = models.ForeignKey(
        ApplyJob, related_name='conversationmessages', on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        User, related_name='conversationmessages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

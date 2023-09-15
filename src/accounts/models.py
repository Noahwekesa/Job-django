from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# class CustomUser(AbstractUser):
#     USER_TYPES = (
#         ('job_seeker', 'Job Seeker'),
#         ('company', 'Company'),
#     )
#     user_type = models.CharField(max_length=20, choices=USER_TYPES)

# class JobSeeker(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     resume = models.FileField(upload_to='resumes/')

#     def __str__(self):
#         return self.name


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('job_seeker', 'Job Seeker'),
        ('company', 'Company'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    # Add a related_name argument to avoid clashes with auth.User
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',  # This is the related_name
        related_query_name='user',
    )
    
    # Add a related_name argument to avoid clashes with auth.User
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',  # This is the related_name
        related_query_name='user',
    )
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_employer = models.BooleanField(default=False)
    is_jobseeker = models.BooleanField(default=False)

    has_resume = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)




# GENDER_MALE = 'male'
# GENDER_FEMALE = 'Female'

# STATUS_PENDING = 'pending'
# STATUS_APPROVED = 'approved'
# STATUS_REJECTED = 'rejected'
# STATUS_CHOICES = (
#     (STATUS_PENDING, 'pending'),
#     (STATUS_APPROVED, 'approved'),
#     (STATUS_REJECTED, 'rejected')
# )
from django.db import models
from accounts.models import CustomUser

# Create your models here.

#class fields for company
class Company(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    est_date = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='logos/')
    
    def __str__(self):
          return self.name
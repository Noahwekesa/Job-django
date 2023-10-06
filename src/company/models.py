from django.db import models

# Create your models here.
from users.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    est_date = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    website = models.URLField(blank=True, null=True) #oprional field
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    fb_name = models.CharField(max_length=100, blank=True, null=True)  # Optional field
    tw_name = models.CharField(max_length=100, blank=True, null=True)   # Optional field
    logo = models.ImageField(upload_to='company_logo', null=True, blank=True)
    
    def __str__(self):
        return self.name
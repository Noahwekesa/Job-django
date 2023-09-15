from django.db import models
from accounts.models import CustomUser
# Create your models here.
class Resume(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    title =  models.CharField(max_length=100, null=True, blank=True)
    location =  models.CharField(max_length=100, null=True, blank=True)
    # upload cv

    def __str__(self):
        return f'{self.first_name} {self.surname}'
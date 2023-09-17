from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class job(models.Model):
    """
    class for job model
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    posted_date = models.DateField(auto_now_add=True)
    number_of_applicants = models.IntegerField(default=0)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

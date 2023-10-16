from django.contrib import admin
from .models import Job
from .models import Industry, City
# Register your models here.

admin.site.register(Job)
admin.site.register(Industry)
admin.site.register(City)
from django.contrib import admin
from .models import job
from users.models import Jobseekerjobmap
# Register your models here.

admin.site.register(job)

class JobseekerjobmapAdmin(admin.ModelAdmin): 
    model = Jobseekerjobmap

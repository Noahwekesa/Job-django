from django.contrib import admin
from .models import *
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'job_type', 'is_available', 'salary', 'requirements', 'timestamp',)

admin.site.register(Job, JobAdmin)
admin.site.register(ApplyJob)
admin.site.register(Industry)
admin.site.register(City)
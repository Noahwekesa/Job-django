from django.contrib import admin
from .models import Resume
# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'surname', 'job_title', 'location', 'phone_number', 'gender', 'cv', )

admin.site.register(Resume, ResumeAdmin) 
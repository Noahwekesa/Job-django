from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_employer', 'has_resume', 'has_company',)

admin.site.register(User, UserAdmin)  # Register the User model with the admin site

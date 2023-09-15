from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    # Add fields for job seeker registration
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CompanyRegistrationForm(UserCreationForm):
    # Add fields for company registration
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

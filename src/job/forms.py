# job_board_app/forms.py
from django import forms
from .models import job

class AddJobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'  # You can specify the fields you want in the form here

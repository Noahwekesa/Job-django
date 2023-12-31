from django import forms
from .models import Job
from .models import ApplyJob


class  CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'company')

class  UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'company')

class ApplyJobForm(forms.ModelForm):

    class Meta:
        model = ApplyJob

        fields = ('experience', 'content',)

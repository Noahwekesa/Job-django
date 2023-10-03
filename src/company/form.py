from django import forms
from .models import Company

class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        # Fields = ['name', 'address', 'city', 'state', 'zip_code', 'phone', 'email', 'website', 'description', 'logo']
        exclude = ('user',)
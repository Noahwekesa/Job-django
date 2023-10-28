from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from users.models import User
from .form import UpdateCompanyForm
# update company
def update_company(request):
    if request.user.is_jobseeker:
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('dashboard')
    company = Company.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateCompanyForm(request.POST, instance=company) 
        if form.is_valid():
            var = form.save(commit=False)
            form.save()
            user = User.objects.get(id=request.user.id)
            user.has_company = True
            var.save()
            user.save()
            messages.success(request, 'Your company information has been updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UpdateCompanyForm(instance=company)
        context = { 'form': form }
        return render(request, 'company/update_company.html', context)
    
# view company details
def view_company(request, pk):
    company = Company.objects.get(pk=pk)
    context = {
        'company': company
    }
    return render(request, 'company/view_company.html', context)

def company_page(request):
    companys = Company.objects.all()
    context = {'companys': companys}
    return render(request, 'company/allcompanies.html', context)
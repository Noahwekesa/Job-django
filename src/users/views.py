from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate, logout 
from resume.models import Resume
from company.models import Company
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')


#job seeker signup
def jobseeker_signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_jobseeker = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.info(request, 'Your account has been created successfully. Please login to continue.')
            return redirect('login_page')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('jobseeker_signup')
    else:
        form = UserRegistrationForm()
        context = {'form': form}
        return render(request, 'auth/register-jobseeker.html', context)
    
#employer signup
def employer_signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            var = form.save(commit=False)
            var.is_employer = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request, 'Your account has been created successfully. Please login to continue.')
            return redirect('login_page')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('employer_signup')
    else:
        form = UserRegistrationForm()
        context = {'form': form}
        return render(request, 'auth/register-employer.html', context)
    

#login a user
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        #if user is authenticated open dashboard
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, "something went wrong")
            return redirect('login_page')
    else:
        return render(request, 'auth/login.html')
    
#logout a user
def logout_page(request):
    logout(request)
    messages.info(request, "You have been logged out successfully")
    return redirect('login_page')

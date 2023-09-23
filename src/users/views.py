from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
import django.contrib.messages as messages
from django.contrib.auth.models import User
from userprofile.models import Userprofile
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            user_type = request.POST.get('user-type', 'jobseeker')

            if user_type == 'employer':
                userprofile = Userprofile.objects.get(user=user, is_employer=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.get(user=user, is_employer=False)
                userprofile.save()

            login(request, user)

            messages.success(request, 'Registration successful.')
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html')


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Handle the case where the user does not exist
            messages.error(request, 'User does not exist.')
            return redirect('login')  # Redirect back to the login page

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials.')

    context = {}
    return render(request, 'auth/login.html', context)
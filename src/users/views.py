from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import django.contrib.messages as messages
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

            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import CustomUser  # Import your CustomUser model

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Store user_type in the CustomUser model
        custom_user = CustomUser(user=user, user_type=user_type)# Adjust based on your CustomUser model
        custom_user.save()
        # Redirect to a success page or dashboard
        return redirect('login')  # Replace 'dashboard' with your desired URL

    return render(request, 'auth/register.html')

def login(request):
    return render(request, 'auth/login.html')
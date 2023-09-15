from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import CustomUser  # Import your CustomUser model
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user_type = request.POST.get('user_type')

#         # Create a new user
#         user_type = User.objects.create_user(username=username, email=email, password=password)

#         # Store user_type in the CustomUser model
#         # custom_user = CustomUser(user=user, user_type=user_type) 
#         custom_user = CustomUser.objects.create(user_type=user_type)  # user_type based on your CustomUser model
#         custom_user.save()
#         # Redirect to a success page or dashboard
#         return redirect('login_page')  # Replace 'dashboard' with your desired URL
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        # Check if a user with the provided username or email already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, 'User with this username or email already exists. Please choose another.')
            return redirect('login_page')

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Store user_type in the CustomUser model
        custom_user = CustomUser.objects.create(user=user, user_type=user_type)  # Adjust based on your CustomUser model

        # Redirect to a success page or dashboard
        return redirect('login_page')  # Replace 'dashboard' with your desired URL

    return render(request, 'auth/register.html')

def login_user(request):
    #Login function
    if request.method == 'POST':
        email =request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username= email, password=password)
        if request.user.user_type == 'job_seeker':
            return redirect('job_seeker-dashboard')
        elif request.user.user_type == 'company':
            return redirect('company-dashboard')
        else:
            return redirect('login_page')
    else:
        messages.warning(request, 'Something went wrong. Please check your credentials.')
    return render(request, 'auth/login.html')

    
    #logout a user
def logout_user(request):
    logout(request)
    messages.info(request, 'Your session has ended.')
    return redirect('login_page')

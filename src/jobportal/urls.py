"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import index, about_page, contact_page, signup, login_page
from django.contrib.auth import views as views
from job.views import job_single
from userprofile.views import dashboard
from job.views import post_job

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', login_page, name='login_page'),
    path('job-single/<int:job_id>/', job_single, name='job_single'),
    path ('dashboard/', dashboard, name='dashboard'),
    path('post_job/', post_job, name='post_job'),
]
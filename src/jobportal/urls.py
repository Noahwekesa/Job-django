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
from users.views import index, about_page, contact_page, login_page, jobseeker_signup, employer_signup, logout_page
from django.contrib.auth import views as views
from dashboard.views import dashboard
from company.views import update_company, view_company
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('jobseeker_signup/', jobseeker_signup, name='jobseeker_signup'),
    path('employer_signup/', employer_signup, name='employer_signup'),
    path('login/', login_page, name='login_page'),
    path('login_out/', logout_page, name='logout_page'),
    path ('dashboard/', dashboard, name='dashboard'),
    path ('update_company/', update_company, name='update_company'),
    path ('view_company/<int:pk>/', view_company, name='view_company'),
]
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
from dashboard.views import dashboard, manage_job
from company.views import update_company, view_company
from resume.views import update_profile, view_profile
from job.views import create_job, update_job, job_listing, job_details, Appy_to_Job, candidates_list, applied_jobs, delete_job

from django.conf import settings
from django.conf.urls.static import static

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
    path ('create_profile/', update_profile, name='update_profile'),
   
    path('view_profile/', view_profile, name='view_profile'),

    #create job
    path ('create_job/', create_job, name='post-job'),

    #update job
    path ('update_job/<int:pk>/', update_job, name='update_job'),

    #view job listing
    path ('job_listing/', job_listing, name='job_listing'),
    
    #view job details
    path ('job_details/<int:pk>/', job_details, name='job-details'),
    
    #manage job
    path ('manage-job/', manage_job, name='manage-job'),

    #apply to job
    path ('apply-to-job/<int:pk>/', Appy_to_Job, name='apply-to-job'),
    
    #show all candidates
    path('candidates_list/<int:pk>/', candidates_list, name='jobseekers'),

    #applied jobs
     path('applied-jobs/', applied_jobs, name='applied-jobs'),

     #delete jobs
     path ('job/<int:id>/', delete_job, name='delete-job'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,   document_root=settings.MEDIA_ROOT)
from django.shortcuts import render, redirect
from job.models import Job
# Create your views here.
def dashboard(request):
    return render(request, 'Dashboard/dashboard.html')


#manages the job on dashaboard creatd by company
def manage_job(request):
        jobs = Job.objects.filter(user=request.user, company=request.user.company)
        context = {'jobs': jobs}
        return render(request, 'Dashboard/manage-job.html', context)
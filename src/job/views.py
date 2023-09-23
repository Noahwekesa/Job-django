from django.shortcuts import render, redirect
from .models import job
from job.forms import AddJobForm
from django.contrib.auth.decorators import login_required
# Create your views here.
# def index(request):
#     jobs = job.objects.all()[0:3]
#     context = {'jobs': jobs}
#     return render(request, 'index.html', context)
def job_single(request, job_id):
    job_single = job.objects.get(pk= job_id)
    return render(request, 'job/job_single.html', {'jobs':job_single})

@login_required
def post_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            job =form.save(commit=False)
            job.created_by = request.user
            # Save the job listing to the database
            job_listing = form.save()
            return redirect('dashboard')  # Redirect to a success page or job detail page
    else:
        form = AddJobForm()
    return render(request, 'job/post-job.html' , {'form': form})
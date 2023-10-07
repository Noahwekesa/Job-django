from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job
from .form import CreateJobForm, UpdateJobForm

# Create your views here.
def create_job(request):
    if request.user.is_jobseeker:
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('dashboard')
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.company = request.user.company
            var.save()
            messages.success(request, 'Job created successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Something went wrong.')
            return redirect('dashboard')
    else:
        form = CreateJobForm()
        return render(request, 'job/create_job.html', {'form': form})
    

def update_job(request, pk):
    Job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job Updated successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Something went wrong.')
            return redirect('dashboard')
    else:
        form = UpdateJobForm()
        return render(request, 'job/update_job.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job
from .form import CreateJobForm, UpdateJobForm

# Create your views here.
def create_job(request):
    if request.user.is_employer and request.user.has_company:
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
                return redirect('post-job')
        else:
            form = CreateJobForm()
            context = {'form': form}
            return render(request, 'job/post-job.html', context)
    else:
        messages.error(request, 'You need to create a company first.')
        return redirect('create_company')
        

def update_job(request, pk):
    job = Job.objects.get(pk=pk)
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
        form = UpdateJobForm(insatance=job)
        context = {'form': form}
        return render(request, 'job/update_job.html', context)


def job_listing(request):
    jobs = Job.objects.filter(is_available=True)
    context = {'jobs': jobs}
    return render(request, 'job/job_listing.html', context)

def job_details(request, pk):
    job = Job.objects.get(pk=pk)
    context = {'job': job}
    return render(request, 'job/job-details.html', context)
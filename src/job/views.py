from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job, ApplyJob
from .form import CreateJobForm, UpdateJobForm
from .filter import JobFilter
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
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    context = {'jobs': jobs}
    return render(request, 'job/job_listing.html', context)

def job_details(request, pk):
    if request.user.is_authenticated:
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            has_applied = True
        else:
            has_applied = False
    else:
        has_applied = False
    job = Job.objects.get(pk=pk)
    context = {'job': job, 'has_applied': has_applied}
    return render(request, 'job/job-details.html', context)

def Appy_to_Job(request, pk):
    if request.user.is_authenticated and request.user.is_jobseeker:
        job = Job.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            messages.info(request, 'You have already applied for this job.')
            return redirect('dashboard')
        else:
            ApplyJob.objects.create(
                job=job,
                user = request.user,
                status = 'Pending'
            )
            messages.success(request, 'Your application has been submitted.')
            return redirect('dashboard')
    if request.user.is_authenticated and request.user.is_employer:
        messages.info(request, 'You are not allowed to apply for jobs. Sign Up as Jobsseeker to apply for jobs.')
        return redirect('dashboard')
    else:
        messages.info(request, 'Please login or register  as a jobseeker to apply for jobs')
        return redirect('login_page')
    
def candidates_list(request, pk):
    job =Job.objects.get(pk=pk)
    jobseeker = job.applyjob_set.all()
    context ={'job': job, 'jobseeker': jobseeker} 
    return render(request, 'job/all_jobseekers.html', context)

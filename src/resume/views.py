from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Resume
from users.models import User
from .form import ResumeForm
# Create your views here.

def update_profile(request):
    if request.user.is_employer:
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('dashboard')
    resume = Resume.objects.get(user=request.user)
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            var = form.save(commit=False)
            user = User.objects.get(pk=request.user.id)
            user.has_resume = True
            user.save()
            var.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Something went wrong!')
    else:
        form = ResumeForm(instance=resume)
        context = {'form': form}
        return render(request, 'jobseekers/update_profile.html', context)  
    
def view_profile(request, pk):
    resume = Resume.objects.get(pk=pk)
    contest = {'resume': resume}
    return render(request, 'Jobseeker/view_profile.html', contest)
from django.shortcuts import render, get_object_or_404, redirect
from job.models import Job
 # Import the correct path to your SkillsFilter
from django.contrib.auth.decorators import login_required
from job.models import Job, ApplyJob, ConversationMessage


# Create your views here.
def dashboard(request):
       jobs = Job.objects.filter(applyjob__user=request.user)
       context = {'jobs': jobs}
       return render(request, 'Dashboard/dashboard.html', context)


#manages the job on dashaboard creatd by company
def manage_job(request):
        jobs = Job.objects.filter(user=request.user, company=request.user.company)
        context = {'jobs': jobs}
        return render(request, 'Dashboard/manage-job.html', context)

@login_required
def view_application(request, applyjob_id):
    if request.user.is_employer:
        applyjob = get_object_or_404(ApplyJob, pk=applyjob_id, job__user=request.user)
    else:
        applyjob = get_object_or_404(ApplyJob, pk=applyjob_id, user=request.user)
        
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            conversationmessage = ConversationMessage.objects.create(applyjob=applyjob, content=content, user=request.user)
            return redirect('view_application', applyjob_id=applyjob_id)  # Use applyjob_id as the parameter name
    
    return render(request, 'Dashboard/view_application.html', {'applyjob': applyjob})
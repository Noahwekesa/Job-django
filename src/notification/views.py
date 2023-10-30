from django.shortcuts import render, redirect
from .models import Notification
from django.contrib.auth.decorators import login_required

@login_required
# def notifications(request):
#     goto = request.GET.get('goto', '' )
#     notification_id = request.GET.get('notification', 0)
#     extra_id = request.GET.get('extra_id', 0)

#     if goto != '':
#         notification = Notification.objects.get(pk=notification_id)
#         notification.is_read = True
#         notification.save()

#         if notification.notification_type == Notification.MESSAGE:
#             if request.user.is_employer:
#                 return redirect('view_application', applyjob_id=notification.extra_id)
#             if request.user.is_employer:
#                 return redirect('view_application', applyjob_id=notification.extra_id)
#         elif notification.notification_type == Notification.APPLICATION:
#             if request.user.is_employer:
#                 return redirect('view_application', applyjob_id=notification.extra_id)
#     return render(request, 'notification/notifications.html')
def notifications(request):
    goto = request.GET.get('goto', '' )
    notification_id = request.GET.get('notification', 0)
    extra_id = request.GET.get('extra_id', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        # user=request.user,
        notification.save()

        if notification.notification_type == Notification.MESSAGE:
            if request.user.is_employer:
                # Redirect employers to a specific view for messages
                return redirect('view_application', applyjob_id=notification.extra_id)
            elif request.user.is_jobseeker:
                # Redirect job seekers to a different view for messages
                return redirect('view_application', applyjob_id=notification.extra_id)
        elif notification.notification_type == Notification.APPLICATION:
            if request.user.is_employer:
                # Redirect employers to a specific view for applications
                return redirect('view_application', applyjob_id=notification.extra_id)
            elif request.user.is_jobseeker:
                # Redirect job seekers to a different view for applications
                return redirect('view_application', applyjob_id=notification.extra_id)

    return render(request, 'notification/notifications.html')
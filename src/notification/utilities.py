from .models import Notification

def create_notification(request, to_user,  notification_type, extra_id=0):
    notificaiton = Notification.objects.create(to_user=to_user, notification_type=notification_type,  user=request.user, extra_id=extra_id)
from .models import Notification

def create_notification(request, to_user,  notification_type, extra_id=0):
     notificaiton = Notification.objects.create(to_user=to_user, notification_type=notification_type,  user=request.user, extra_id=extra_id)

# def create_message_notification(sender, receiver):
#     Notification.objects.create(to_user=receiver, notification_type=Notification.MESSAGE, user=sender)

# def create_notification(sender, receiver, notification_type, extra_id=0):
#     Notification.objects.create(to_user=receiver, notification_type=notification_type, user=sender, extra_id=extra_id)

# def create_message_notification(sender, receiver):
#     Notification.objects.create(to_user=receiver, notification_type=Notification.MESSAGE, user=sender)

# def create_notification(sender, receiver, notification_type, extra_id=0):
#     Notification.objects.create(to_user=receiver, notification_type=notification_type, user=sender, extra_id=extra_id)

from .models import Notification

def notifications(request):
    if request.user.is_authenticated:
        #gets the notifications from the db 
        return {'notifications': request.user.notifications.filter(is_read=False)}
    else:
        #if empty return an empty list
        return {'notifications': []}
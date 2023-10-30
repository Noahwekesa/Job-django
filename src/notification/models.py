from django.db import models
from users.models import User
# my models

class Notification(models.Model):
    MESSAGE = 'message'
    APPLICATION = 'application'

    CHOICES = (
        (MESSAGE, 'Message'),
        (APPLICATION, 'Application')
    )

    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    user =  models.ForeignKey(User, related_name='creatednotifications', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']
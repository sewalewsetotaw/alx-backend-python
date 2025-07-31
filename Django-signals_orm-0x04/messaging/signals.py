# code
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import Message,Notification,MessageHistory

@receiver(pre_save,sender=Message)
def create_message_history(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:
                # Log the old content to MessageHistory
                MessageHistory.objects.create(
                    message=instance,
                    old_content=old_message.content
                )
                instance.edited = True  
        except Message.DoesNotExist:
            pass 
 
@receiver(post_save, sender=Message) 
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver,message=instance)
 
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Message,Notification,MessageHistory

@receiver(post_save, sender=Message) 
def create_notification(sender, instance, created, **kwargs):
    print('sender',sender)
    print('instance',instance)
    print('created',created)
    if created:
        Notification.objects.create(user=instance.receiver,message=instance)
 
@receiver(pre_save,sender=Message)
def create_message_history(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:
                # Log the old content to MessageHistory
                message_history =MessageHistory.objects.create(
                    message=instance,
                    old_content=old_message.content,
                    edited_by=instance.sender 
                )
                print('message:', message_history.message)
                print('old_content:', message_history.old_content)
                print('edited_by:', message_history.edited_by)
                instance.edited = True  
        except Message.DoesNotExist:
            pass 
 
@receiver(post_delete,sender=User)
def delete_user_related_data(sender,instance,**kwargs):
      print(f"Message instance with ID {instance.id} was deleted.")
      Message.objects.filter(sender=instance).delete()
      Message.objects.filter(receiver=instance).delete()
      Notification.objects.filter(user=instance).delete()
      MessageHistory.objects.filter(message__sender=instance).delete()

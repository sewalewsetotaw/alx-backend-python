from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid 

class User(AbstractUser):
    class UserRole(models.TextChoices):
        GUEST = 'guest', 'Guest'
        HOST = 'host', 'Host'
        ADMIN = 'admin', 'Admin'
    user_id  = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False,
                            db_index=True)
    # first_name =models.CharField(max_length=155, null=False)
    # last_name  =models.CharField(max_length=155,null=False)
    email  =models.EmailField(unique=True,null=False)
    # password_hash  =models.CharField(max_length=255,null=False)
    phone_number  =models.CharField(max_length=255,null=True)
    role=models.CharField(max_length=15,choices=UserRole.choices,null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['first_name','last_name']
    def __str__(self):
            return f"{self.email}"

class Conversation(models.Model):
    conversation_id =models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False,
                            db_index=True)
    participants =models.ManyToManyField(User,related_name='conversations')
    created_at=models.DateTimeField(auto_now_add=True)
       
    def __str__(self):
          return f"Conversation {self.conversation_id}"
class Message(models.Model):
    message_id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False,
                            db_index=True)
    sender=models.ForeignKey(User,on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body=models.TextField(null=False)
    sent_at=models.DateTimeField(auto_now_add=True)
       
    def __str__(self):
          return f"Message {self.message_id} from {self.sender.email}"

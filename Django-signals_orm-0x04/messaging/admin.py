from django.contrib import admin

# Register your models here.
from .models import Message,MessageHistory,Notification

admin.site.register(Message)
admin.site.register(MessageHistory)
admin.site.register(Notification)
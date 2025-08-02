from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from .models import Message, Notification, MessageHistory
from django.contrib.auth.models import User

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access if the user is either the sender or receiver of a Message,
    or the recipient of a Notification, or the sender/receiver of the original Message in MessageHistory.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Message):
            return request.user == obj.sender or request.user == obj.receiver

        elif isinstance(obj, Notification):
            return request.user == obj.user

        elif isinstance(obj, MessageHistory):
            return request.user == obj.message.sender or request.user == obj.message.receiver
        elif isinstance(obj, User):
            return request.user == obj 
        return False

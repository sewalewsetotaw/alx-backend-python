from rest_framework import viewsets, filters, status
from .models import  Message, MessageHistory,Notification
from django.contrib.auth.models import User
from .serializers import UserSerializer,MessageSerializer, MessageHistorySerializer,NotificationSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsParticipantOfConversation
from django.contrib.auth import logout
from django.shortcuts import redirect

class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsParticipantOfConversation)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
class NotificationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsParticipantOfConversation)
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class MessageHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsParticipantOfConversation)
    queryset = MessageHistory.objects.all()
    serializer_class = MessageHistorySerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsParticipantOfConversation)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete_user(request):
        user = request.user
        logout(request)
        user.delete()
        return redirect('/')
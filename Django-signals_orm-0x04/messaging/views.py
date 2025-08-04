from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import viewsets, filters, status
from .models import  Message, MessageHistory,Notification
from django.contrib.auth.models import User
from .serializers import UserSerializer,MessageSerializer, MessageHistorySerializer,NotificationSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsParticipantOfConversation
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models import Prefetch
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, redirect

@method_decorator(cache_page(60), name='dispatch')
class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(request):
        """
        View to fetch messages sent by the logged-in user,
        including related receiver, editor, parent message,
        and prefetch replies for optimized DB queries.
        """
        messages_qs = Message.objects.filter(sender=request.user).select_related(
            'receiver', 'edited_by', 'parent_message'
        ).prefetch_related(
            'replies'
        ).order_by('-timestamp')

        context = {
            'messages': messages_qs
        }
        return render(request, 'messaging/user_messages.html', context)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
    
    @action(detail=False, methods=['get'], url_path='unread')
    def unread_messages(self, request):
        user = request.user
        unread_messages = Message.unread.unread_for_user(user).select_related('sender', 'receiver').only('id', 'sender_id', 'receiver_id', 'content', 'timestamp').order_by('timestamp')
        serializer = self.get_serializer(unread_messages, many=True)
        return Response(serializer.data)
class NotificationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    queryset = Notification.objects.select_related('user', 'message__sender').all()
    serializer_class = NotificationSerializer

class MessageHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    queryset = MessageHistory.objects.select_related('message', 'edited_by').all()
    serializer_class = MessageHistorySerializer
 
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['delete'], url_path='delete-account')
    def delete_user(self, request):
        user = request.user
        logout(request)
        user.delete()
        return Response({'detail': 'Account deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
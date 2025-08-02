from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from .views import UserViewSet,MessageViewSet,MessageHistoryViewSet,NotificationViewSet
from django.contrib.auth.models import User

router = routers.DefaultRouter()
router.register(r'messagehistories', MessageHistoryViewSet, basename='messagehistory') 
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'messages', MessageViewSet, basename='message')

router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory


class MessagingSignalTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='sender', password='pass')
        self.receiver = User.objects.create_user(username='receiver', password='pass')

    def test_notification_created_on_message_send(self):
        msg = Message.objects.create(sender=self.sender, receiver=self.receiver, content='Hello')
        self.assertEqual(Notification.objects.filter(user=self.receiver, message=msg).count(), 1)

    def test_message_edit_history(self):
        msg = Message.objects.create(sender=self.sender, receiver=self.receiver, content='Initial')
        msg.content = 'Edited'
        msg.save()
        self.assertTrue(msg.edited)
        self.assertEqual(MessageHistory.objects.filter(message=msg).count(), 1)

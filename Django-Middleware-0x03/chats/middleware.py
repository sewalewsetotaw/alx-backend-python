# chats/middleware.py

from datetime import datetime
import time
from django.http import HttpResponseForbidden,JsonResponse
import logging
from collections import defaultdict

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Set up logging to file
        self.logger = logging.getLogger("request_logger")
        handler = logging.FileHandler("requests.log")
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        self.logger.info(log_message)

        return self.get_response(request)
class RestrictAccessByTimeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        current_hour=datetime.now().hour
        if not(18<=current_hour<=21):
            return HttpResponseForbidden("Chat access is only allowed between 6 PM and 9 PM.")
        return self.get_response(request) 
    
class OffensiveLanguageMiddleware:
        def __init__(self,get_response):
             self.get_response=get_response
             self.ip_message_log = defaultdict(list)
             self.MESSAGE_LIMIT = 5
             self.TIME_WINDOW = 60  # seconds
        def __call__(self, request):
         if request.method == "POST" and request.path.startswith("/api/messages/"):
            ip = self.get_client_ip(request)
            current_time = time.time()
            recent_requests = [
                t for t in self.ip_message_log[ip]
                if current_time - t < self.TIME_WINDOW
            ]
            self.ip_message_log[ip] = recent_requests

            if len(recent_requests) >= self.MESSAGE_LIMIT:
                return JsonResponse(
                    {
                        "error": "Too many messages. Limit is 5 messages per minute."
                    },
                    status=429
                )
            self.ip_message_log[ip].append(current_time)
         return self.get_response(request)
        def get_client_ip(self, request):
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                return x_forwarded_for.split(',')[0].strip()
            return request.META.get('REMOTE_ADDR')
class RolepermissionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
         if request.method == "POST" and request.path.startswith("/api/messages/"):
            user = request.user
            user_role = getattr(user, "role", None)
            if user_role not in ["admin", "moderator"]:
                return JsonResponse(
                    {"error": "Forbidden: insufficient role permission."},
                    status=403
                )
         return self.get_response(request)
    


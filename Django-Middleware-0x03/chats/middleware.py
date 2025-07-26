# chats/middleware.py

from datetime import datetime
from django.http import HttpResponseForbidden
import logging

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

        response = self.get_response(request)
        return response
class RestrictAccessByTimeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        current_hour=datetime.now().hour
        if(18<=current_hour<=21):
            return HttpResponseForbidden("Chat access is only allowed between 6 PM and 9 PM.")
        return self.get_response(request)
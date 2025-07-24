from rest_framework import permissions

class IsParticipantOrReadOnly(permissions.BasePermission):
    """
    Allow access only to conversation participants
    """

    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()

from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        # Autorise uniquement si l'utilisateur est admin
        return request.user and request.user.is_staff

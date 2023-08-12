# accounts/permissions.py

from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user.role.role)  # Add this line
        return request.user.role.role == 'admin'

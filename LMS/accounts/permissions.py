# accounts/permissions.py

"""
from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user.role.role)  # Add this line
        return request.user.role.role == 'admin'
"""

# accounts/permissions.py
from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role.role == 'admin':
            return True
        return False


# accounts/permissions.py
class IsInstructorUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role.role == 'instructor':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role.role == 'instructor':
            return True
        return False


class IsLearnerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role.role == 'learner':
            return True
        return False
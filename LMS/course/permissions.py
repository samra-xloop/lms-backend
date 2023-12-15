from rest_framework import permissions
from course.models import *
from django.db.models import Q

class CreateAuthorORCoursePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has permission to create a module
        return request.user.role.role in ['admin', 'instructor']
    
class AuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin or the instructor who created the author
        if request.user.role.role =='admin' or (request.user.role.role == 'instructor' and obj.created_by == request.user):
            return True
        
        if request.user in obj.editor.all():
            return True
        
        return False    

class CreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True

        # Check if the user is an instructor and is in the 'created_by' field of the related author
        if request.user.role.role == 'instructor':
            instructor = Author.objects.get(id=request.data.get('instructor')) 
            if instructor.created_by == request.user or request.user in instructor.editor.all():
                return True
        
        return False

class EditORDeletePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor':
            if (
                (request.user == obj.instructor.created_by) or
                (request.user in obj.instructor.editor.all())
            ):
                return True
        return False

from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False



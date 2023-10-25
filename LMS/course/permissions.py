from rest_framework import permissions
from course.models import *
from django.db.models import Q
#  class AuthorPermission(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # Check if the user is an admin or the instructor who created the author
#         return request.user.role.role =='admin' or (request.user.role.role == 'instructor' and obj.author == request.user)
class CategoryPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin or the instructor who created the category
        # return request.user.role.role =='admin' or (request.user.role.role == 'instructor' and obj.created_by == request.user)
        return request.user.role.role =='admin' or request.user.role.role == 'instructor'
class CreateCoursePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has permission to create a module
        return request.user.role.role in ['admin', 'instructor']
        # def has_permission(self, request, view):
        # # Check if the user has permission to create a module
        #     if request.user.role.role == 'admin' or (
        #         request.user.role.role == 'instructor' and
        #         (
        #         (request.data.get('course') and
        #          request.user == course.created_by) or
        #         (request.data.get('course') and
        #          request.user in course.editor.all())
        #        )
        #     ):
        #         return True
        #     return False
    # def has_permission(self, request, view):
    #     # Check if the user has permission to create a module
    #     if request.user.role.role == 'admin':
    #         return True
    #     if request.user.role.role == 'instructor':
    #         # Check if the user is in the 'created_by' field of the related course or in the 'editor' field
    #         if request.data.get('course'):
    #             course = Course.objects.get(pk=request.data['course'])
    #             return (
    #                 request.user == course.created_by or
    #                 request.user in course.editor.all()
    #             )
    #     return False
class EditCoursePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user has permission to edit the module
        # if request.user.role.role in ['admin', 'instructor']:
        #     return True
        if request.user.role.role =='admin' or (request.user.role.role == 'instructor' and obj.created_by == request.user):
            return True
        # Check if the user is the creator of the module
        # if obj.created_by == request.user:
        #     return True
        # Check if the user is in the list of editors
        if request.user in obj.editor.all():
            return True
        return False
# class ListPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Check if the user has permission to list courses
#         if request.user.role.role in ['admin', 'learner']:
#             return True
#         if request.user.role.role == 'instructor':
#             # Filter courses where the user is the creator or in the editor field
#             courses = Course.objects.filter(Q(created_by=request.user) | Q(editor=request.user))
#             # Return True if there are any matching courses
#             return courses.exists()
#         return False
# class ListPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Check if the user has permission to list courses
#         if request.user.role.role in ['admin', 'learner']:
#             return True
#         if request.user.role.role == 'instructor':
#             # Filter courses where the user is the creator
#             created_courses = Course.objects.filter(created_by=request.user)
#             # Filter courses where the user is in the editor field
#             edited_courses = Course.objects.filter(editor=request.user)
#             # Combine the two querysets and check if there are any matching courses
#             courses = created_courses | edited_courses
#             # Return True if there are any matching courses
#             return courses.exists()
#         return False
# class ListPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Check if the user has permission to list courses
#         if request.user.role.role in ['admin', 'learner']:
#             return True
#         if request.user.role.role == 'instructor':
#             # Check if the user created any courses
#             created_courses = Course.objects.filter(created_by=request.user)
#             # Check if the user is in the editor field of any course
#             edited_courses = Course.objects.filter(editor=request.user)
#             # Return True if the user is either the creator or in the editor field of any course
#             return created_courses.exists() or edited_courses.exists()
#         return False
# class ListPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Check if the user has permission to list courses
#         if request.user.role.role in ['admin', 'learner']:
#             return True
#         if request.user.role.role == 'instructor':
#             # Check if the user created any courses
#             created_courses = Course.objects.filter(created_by=request.user)
#             if created_courses.exists():
#                 return True
#             # Check if the user is in the editor field of any course
#             edited_courses = Course.objects.filter(editor=request.user)
#             if edited_courses.exists():
#                 return True
#         return False
class ListCoursePermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Check if the user has permission to list modules
#         if request.user.role.role in ['admin', 'instructor', 'learner']:
#             return True
    def has_object_permission(self, request, view, obj):
        # Check if the user has permission to edit the module
        # if request.user.role.role in ['admin', 'instructor']:
        #     return True
        if request.user.role.role =='admin' or (request.user.role.role == 'instructor' and obj.created_by == request.user):
            return True
        # Check if the user is the creator of the module
        if obj.created_by == request.user:
            return True
        # Check if the user is in the list of editors
        if request.user in obj.editor.all():
            return True
        if request.user.role.role == 'learner':
            return True
        return False
# class ListPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Check if the user has permission to list courses
#         user = request.user
#         # Check if the user is an admin
#         if user.role.role == 'admin':
#             return True
#         # Check if the user is an instructor who created any of the courses
#         created_courses = Course.objects.filter(obj.created_by==user)
#         if created_courses.exists():
#             return True
#         # Check if the user is an instructor who is part of the editor field for any course
#         edited_courses = Course.objects.filter(editor=user)
#         if edited_courses.exists():
#             return True
#         # Check if the user is a learner
#         if user.role.role == 'learner':
#             return True
#         return False
class DeleteCoursePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user has permission to delete the module
        if request.user.role.role == 'admin':
            return True
        # Check if the user is the creator of the module
        if obj.created_by == request.user:
            return True
        return False
class CreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor' and request.data.get('course'):
            course = Course.objects.get(pk=request.data['course'])
            if (
                (request.user == course.created_by) or
                (request.user in course.editor.all())
            ):
                return True
        return False
        
class EditPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor':
            if (
                (request.user == obj.course.created_by) or
                (request.user in obj.course.editor.all())
            ):
                return True
        return False
    
class ListPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor':
            if (
                (request.user == obj.created_by) or
                (request.user in obj.editor.all())
            ):
                return True
        # Check if the user is a learner
        if request.user.role.role == 'learner':
            return True
        return False
class DeletePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor':
            if (
                (request.user == obj.course.created_by) or
                (request.user in obj.course.editor.all())
            ):
                return True
        return False
    
class CreateUnitPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor' and request.data.get('module'):
            module = Module.objects.get(pk=request.data['module'])
            if (
                (request.user == module.created_by) or
                (request.user in module.editor.all())
            ):
                return True
        return False    
    
class EditUnitPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor':
            if (
                (request.user == obj.module.created_by) or
                (request.user in obj.module.editor.all())
            ):
                return True
        return False
    
class ListUnitPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor':
            if (
                (request.user == obj.created_by) or
                (request.user in obj.editor.all())
            ):
                return True
        # Check if the user is a learner
        if request.user.role.role == 'learner':
            return True
        return False
class DeleteUnitPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor':
            if (
                (request.user == obj.module.created_by) or
                (request.user in obj.module.editor.all())
            ):
                return True
        return False    

class CreateContentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor' and request.data.get('unit'):
            unit = Unit.objects.get(pk=request.data['unit'])
            if (
                (request.user == unit.created_by) or
                (request.user in unit.editor.all())
            ):
                return True
        return False    
    
class EditContentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor':
            if (
                (request.user == obj.unit.created_by) or
                (request.user in obj.unit.editor.all())
            ):
                return True
        return False
    
class ListContentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor':
            if (
                (request.user == obj.created_by) or
                (request.user in obj.editor.all())
            ):
                return True
        # Check if the user is a learner
        if request.user.role.role == 'learner':
            return True
        return False
class DeleteContentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor':
            if (
                (request.user == obj.unit.created_by) or
                (request.user in obj.unit.editor.all())
            ):
                return True
        return False
    
class CreateGradingPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor' and request.data.get('assignment'):
            assignmnet = Assignment.objects.get(pk=request.data['assignment'])
            if (
                (request.user == assignmnet.created_by) or
                (request.user in assignmnet.editor.all())
            ):
                return True
        return False    
    
class EditGradingPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor':
            if (
                (request.user == obj.assignment.created_by) or
                (request.user in obj.assignment.editor.all())
            ):
                return True
        return False
    
class ListGradingPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor':
            if (
                (request.user == obj.created_by) or
                (request.user in obj.editor.all())
            ):
                return True
        # Check if the user is a learner
        if request.user.role.role == 'learner':
            return True
        return False
class DeleteGradingPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.role.role == 'admin':
            return True
        # Check if the user is an instructor and is in the 'created_by' field of the related course or in the 'editor' list
        if request.user.role.role == 'instructor':
            if (
                (request.user == obj.assignment_submission.created_by) or
                (request.user in obj.assignment_submission.editor.all())
            ):
                return True
        return False
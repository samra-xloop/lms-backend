# """
# File: permissions.py
# Author: Muhammad Humza
# Date: 09-08-2023
# Description: This module contains custom permission classes for the accounts app.

# This module defines custom permission classes for checking user roles (admin, instructor, learner) in the application.

# """
# from rest_framework import permissions

# class IsAdminUser(permissions.BasePermission):
#     """
#     Permission class to check if the user has admin role.

#     Methods:
#         has_permission: Returns True if the user has an admin role, False otherwise.

#     """
#     def has_permission(self, request, view):
#         """
#          Check if the user has an admin role.

#         Args:
#             request (HttpRequest): The request object.
#             view (APIView): The view object.

#         Returns:
#             bool: True if the user has an admin role, False otherwise.
#         """
#         if request.user.role.role == 'admin':
#             return True
#         return False



# class IsInstructorUser(permissions.BasePermission):
#     """
#         Permission class to check if the user has instructor role.

#         Methods:
#             has_permission: Returns True if the user has an instructor role, False otherwise.
#             has_object_permission: Returns True if the user has an instructor role for an object, False otherwise.
#     """
#     def has_permission(self, request, view):
#         """
#         Check if the user has an instructor role.

#         Args:
#             request (HttpRequest): The request object.
#             view (APIView): The view object.

#         Returns:
#             bool: True if the user has an instructor role, False otherwise.
#         """
#         if request.user.role.role == 'instructor':
#             return True
#         return False

#     def has_object_permission(self, request, view, obj):
#         """
#          Check if the user has an instructor role for a specific object.

#         Args:
#             request (HttpRequest): The request object.
#             view (APIView): The view object.
#             obj: The object to check permissions for.

#         Returns:
#             bool: True if the user has an instructor role for the object, False otherwise.
#         """
#         if request.user.role.role == 'instructor':
#             return True
#         return False


# class IsLearnerUser(permissions.BasePermission):
#     """
     
#         Permission class to check if the user has learner role.

#         Methods:
#             has_permission: Returns True if the user has a learner role, False otherwise.

    
#     """
#     def has_permission(self, request, view):
#         """
#         Check if the user has a learner role.

#         Args:
#             request (HttpRequest): The request object.
#             view (APIView): The view object.

#         Returns:
#             bool: True if the user has a learner role, False otherwise
#         """
#         if request.user.role.role == 'learner':
#             return True
#         return False
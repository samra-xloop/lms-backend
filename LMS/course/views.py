from argparse import _ActionsContainer
from course.models import *
from .serializers import *
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from accounts.permissions import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from course.permissions import *
# Create your views here.

# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

#     def create(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to create courses.'}, status=status.HTTP_403_FORBIDDEN)
            
#             serializer = AuthorSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def get_queryset(self):
#         user = self.request.user

#         # Example: Filter queryset based on user's role
#         if user.role.role in ['admin','instructor']:
#             return Author.objects.all()
#         # else:
#         #     # Filter queryset for non-admin users
#         #     return Course.objects.filter(user=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         if not queryset.exists():
#             # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
#             return Response([], status=status.HTTP_404_NOT_FOUND)


#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#         # Override the update method to check permissions
#     def update(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to update courses.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return super().update(request, *args, **kwargs)
        

#     def destroy(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to delete courses.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

#     def create(self, request, *args, **kwargs):
#         # Check if the requesting user has an 'admin' or 'instructor' role
#         if request.user.role.role not in ['admin', 'instructor']:
#             return Response({'detail': 'You do not have permission to create authors.'}, status=status.HTTP_403_FORBIDDEN)

#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def list(self, request, *args, **kwargs):
#         # Apply the custom permission class for listing authors
#         self.permission_classes = [permissions.IsAuthenticated, AuthorPermission]

#         # Check if the requesting user has permission to list authors
#         if not AuthorPermission().has_object_permission(request, self, Author()):
#             return Response({'detail': 'You do not have permission to list authors.'}, status=status.HTTP_403_FORBIDDEN)

#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#     def update(self, request, *args, **kwargs):
#         # Apply the custom permission class for editing authors
#         self.permission_classes = [permissions.IsAuthenticated, AuthorPermission]

#         # Check if the requesting user has permission to edit the author
#         if not AuthorPermission().has_object_permission(request, self, self.get_object()):
#             return Response({'detail': 'You do not have permission to edit this author.'}, status=status.HTTP_403_FORBIDDEN)

#         return super().update(request, *args, **kwargs)

#     def destroy(self, request, *args, **kwargs):
#         # Apply the custom permission class for deleting authors
#         self.permission_classes = [permissions.IsAuthenticated, AuthorPermission]

#         # Check if the requesting user has permission to delete the author
#         if not AuthorPermission().has_object_permission(request, self, self.get_object()):
#             return Response({'detail': 'You do not have permission to delete this author.'}, status=status.HTTP_403_FORBIDDEN)

#         return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations
    def create(self, request, *args, **kwargs):
        # Check if the requesting user has an 'admin' or 'instructor' role
        if request.user.role.role not in ['admin']:
            return Response({'detail': 'You do not have permission to create categories.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def list(self, request, *args, **kwargs):
        # Apply the custom permission class for listing categories
        self.permission_classes = [permissions.IsAuthenticated, CategoryPermission]
        # Check if the requesting user has permission to list categories
        if not CategoryPermission().has_object_permission(request, self, Category()):
            return Response({'detail': 'You do not have permission to list categories.'}, status=status.HTTP_403_FORBIDDEN)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        # Apply the custom permission class for editing categories
        # self.permission_classes = [permissions.IsAuthenticated, CategoryPermission]
        # Check if the requesting user has permission to edit the category
        # if not CategoryPermission().has_object_permission(request, self, self.get_object()):
        #     return Response({'detail': 'You do not have permission to edit this category.'}, status=status.HTTP_403_FORBIDDEN)
        if request.user.role.role not in ['admin']:
            return Response({'detail': 'You do not have permission to create categories.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        # Apply the custom permission class for deleting categories
        self.permission_classes = [permissions.IsAuthenticated, CategoryPermission]
        # Check if the requesting user has permission to delete the category
        if not CategoryPermission().has_object_permission(request, self, self.get_object()):
            return Response({'detail': 'You do not have permission to delete this category.'}, status=status.HTTP_403_FORBIDDEN)
        return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# class CategoryViewSet(viewsets.ModelViewSet):
#         queryset = Category.objects.all()
#         serializer_class = CategorySerializer
#         permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

#         def create(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to create categories.'}, status=status.HTTP_403_FORBIDDEN)
            
#             serializer = CategorySerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         # def get(self, request, *args, **kwargs):
#         #     obj = super().get_object()
#         #     # Check if the requesting user has an 'admin' role
#         #     if request.user.role.role != 'admin':
#         #         self.permission_denied(request)

#         #     return obj

#         def get_queryset(self):
#             user = self.request.user

#         # Example: Filter queryset based on user's role
#             if user.role.role in ['admin','learner','instructor']:
#                 return Category.objects.all()
#             # else:
#             # # Filter queryset for non-admin users
#             #     return Category.objects.filter(user=user)

#         def list(self, request, *args, **kwargs):
#             queryset = self.filter_queryset(self.get_queryset())

#             if not queryset.exists():
#                 # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
#                 return Response([], status=status.HTTP_404_NOT_FOUND)


#             serializer = self.get_serializer(queryset, many=True)
#             return Response(serializer.data)

#         # Override the update method to check permissions
#         def update(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to update categories.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return super().update(request, *args, **kwargs)
        

#         def destroy(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to delete categories.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,CreateCoursePermission]
        if not CreateCoursePermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to create course.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Handle module creation as before
    def update(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,EditCoursePermission]
        if not EditCoursePermission().has_object_permission(request, self, self.get_object()):
            return Response({'detail': 'You do not have permission to update this course.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
        # Handle module update as before
    def list(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,ListCoursePermission]
        if not ListCoursePermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to list course.'}, status=status.HTTP_403_FORBIDDEN)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,DeleteCoursePermission]
        if not DeleteCoursePermission().has_object_permission(request, self, self.get_object()):
                return Response({'detail': 'You do not have permission to delete this course.'}, status=status.HTTP_403_FORBIDDEN)
        return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



# class CourseViewSet(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

#     def create(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to create courses.'}, status=status.HTTP_403_FORBIDDEN)
            
#             serializer = CourseSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def get_queryset(self):
#         user = self.request.user

#         # Example: Filter queryset based on user's role
#         if user.role.role in ['admin','instructor','learner']:
#             return Course.objects.all()
#         # else:
#         #     # Filter queryset for non-admin users
#         #     return Course.objects.filter(user=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         if not queryset.exists():
#             # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
#             return Response([], status=status.HTTP_404_NOT_FOUND)


#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#         # Override the update method to check permissions
#     def update(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to update courses.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return super().update(request, *args, **kwargs)
        

#     def destroy(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to delete courses.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     self.permission_classes = [permissions.IsAuthenticated,CreatePermission]
    #     if not CreatePermission().has_permission(request, self):
    #             return Response({'detail': 'You do not have permission to create modules.'}, status=status.HTTP_403_FORBIDDEN)
    #     serializer = ModuleSerializer(data=request.data)
    #     if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     # Handle module creation as before
    def create(self, request, *args, **kwargs):
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            # Check if the user can create a module
            if not CreatePermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to create modules.'}, status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def update(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,EditPermission]

        if not EditPermission().has_object_permission(request, self, self.get_object()):
            return Response({'detail': 'You do not have permission to update this module.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

        # Handle module update as before

    def list(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,ListPermission]
        if not ListPermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to list modules.'}, status=status.HTTP_403_FORBIDDEN)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,DeletePermission]
        if not DeletePermission().has_object_permission(request, self, self.get_object()):
                return Response({'detail': 'You do not have permission to delete this module.'}, status=status.HTTP_403_FORBIDDEN)
        
        return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        # Handle module deletion as before

    # Other methods and views



# class ModuleViewSet(viewsets.ModelViewSet):
#     queryset = Module.objects.all()
#     serializer_class = ModuleSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

#     def create(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to create modules.'}, status=status.HTTP_403_FORBIDDEN)
            
#             serializer = ModuleSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def get_queryset(self):
#         user = self.request.user

#         # Example: Filter queryset based on user's role
#         if user.role.role in ['admin','instructor','learner']:
#             return Module.objects.all()
#         # else:
#         #     # Filter queryset for non-admin users
#         #     return Module.objects.filter(user=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         if not queryset.exists():
#             # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
#             return Response([], status=status.HTTP_404_NOT_FOUND)


#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#         # Override the update method to check permissions
#     def update(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to update modules.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return super().update(request, *args, **kwargs)
        

#     def destroy(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to delete modules.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,CreateUnitPermission]
        if not CreateUnitPermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to create unit.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Handle module creation as before

    def update(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,EditUnitPermission]

        if not EditUnitPermission().has_object_permission(request, self, self.get_object()):
            return Response({'detail': 'You do not have permission to update this unit.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

        # Handle module update as before

    def list(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,ListUnitPermission]
        if not ListUnitPermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to list units.'}, status=status.HTTP_403_FORBIDDEN)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,DeleteUnitPermission]
        if not DeleteUnitPermission().has_object_permission(request, self, self.get_object()):
                return Response({'detail': 'You do not have permission to delete this unit.'}, status=status.HTTP_403_FORBIDDEN)
        
        return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# class UnitViewSet(viewsets.ModelViewSet):
#     queryset = Unit.objects.all()
#     serializer_class = UnitSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

#     def create(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to create units.'}, status=status.HTTP_403_FORBIDDEN)
            
#             serializer = UnitSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def get_queryset(self):
#         user = self.request.user

#         # Example: Filter queryset based on user's role
#         if user.role.role in ['admin','instructor','learner']:
#             return Unit.objects.all()
#         # else:
#         #     # Filter queryset for non-admin users
#         #     return Unit.objects.filter(user=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         if not queryset.exists():
#             # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
#             return Response([], status=status.HTTP_404_NOT_FOUND)


#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#         # Override the update method to check permissions
#     def update(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to update units.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return super().update(request, *args, **kwargs)
        

#     def destroy(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to delete units.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,CreateContentPermission]
        if not CreateContentPermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to create videos.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Handle module creation as before

    def update(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,EditContentPermission]

        if not EditContentPermission().has_object_permission(request, self, self.get_object()):
            return Response({'detail': 'You do not have permission to update this video.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

        # Handle module update as before

    def list(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,ListContentPermission]
        if not ListContentPermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to list videos.'}, status=status.HTTP_403_FORBIDDEN)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,DeleteContentPermission]
        if not DeleteContentPermission().has_object_permission(request, self, self.get_object()):
                return Response({'detail': 'You do not have permission to delete this video.'}, status=status.HTTP_403_FORBIDDEN)
        
        return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# class VideoViewSet(viewsets.ModelViewSet):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

#     def create(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to create videos.'}, status=status.HTTP_403_FORBIDDEN)
            
#             serializer = VideoSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def get_queryset(self):
#         user = self.request.user

#         # Example: Filter queryset based on user's role
#         if user.role.role in ['admin','instructor','learner']:
#             return Video.objects.all()
#         # else:
#         #     # Filter queryset for non-admin users
#         #     return Video.objects.filter(user=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         if not queryset.exists():
#             # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
#             return Response([], status=status.HTTP_404_NOT_FOUND)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#         # Override the update method to check permissions
#     def update(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to update videos.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return super().update(request, *args, **kwargs)
        

#     def destroy(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to delete videos.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,CreateContentPermission]
        if not CreateContentPermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to create files.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Handle module creation as before

    def update(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,EditContentPermission]

        if not EditContentPermission().has_object_permission(request, self, self.get_object()):
            return Response({'detail': 'You do not have permission to update this file.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

        # Handle module update as before

    def list(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,ListContentPermission]
        if not ListContentPermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to list files.'}, status=status.HTTP_403_FORBIDDEN)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,DeleteContentPermission]
        if not DeleteContentPermission().has_object_permission(request, self, self.get_object()):
                return Response({'detail': 'You do not have permission to delete this file.'}, status=status.HTTP_403_FORBIDDEN)
        
        return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# class FileViewSet(viewsets.ModelViewSet):
#     queryset = File.objects.all()
#     serializer_class = FileSerializer    
#     permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

#     def create(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to create documents.'}, status=status.HTTP_403_FORBIDDEN)
            
#             serializer = FileSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def get_queryset(self):
#         user = self.request.user

#         # Example: Filter queryset based on user's role
#         if user.role.role in ['admin','instructor','learner']:
#             return File.objects.all()
#         # else:
#         #     # Filter queryset for non-admin users
#         #     return File.objects.filter(user=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         if not queryset.exists():
#             # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
#             return Response([], status=status.HTTP_404_NOT_FOUND)


#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#         # Override the update method to check permissions
#     def update(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to update documents.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return super().update(request, *args, **kwargs)
        

#     def destroy(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to delete documents.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# # class QuizViewSet(viewsets.ModelViewSet):
# #     queryset = Quiz.objects.all()
# #     serializer_class = QuizSerializer    

#     # def destroy(self, request, *args, **kwargs):
#     # #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#     #     pass

# # class Quiz_QuestionViewSet(viewsets.ModelViewSet):
# #     queryset = Quiz_Question.objects.all()
# #     serializer_class = Quiz_QuestionSerializer    

#     # def destroy(self, request, *args, **kwargs):
#     # #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#     #     pass

# # class Question_OptionViewSet(viewsets.ModelViewSet):
# #     queryset = Question_Option.objects.all()
# #     serializer_class = Question_OptionSerializer    

#     # def destroy(self, request, *args, **kwargs):
#     # #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#     #     pass

# # class Quiz_SubmissionViewSet(viewsets.ModelViewSet):
# #     queryset = Quiz_Submission.objects.all()
# #     serializer_class = Quiz_SubmissionSerializer    

#     # def destroy(self, request, *args, **kwargs):
#     # #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#     #     pass

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,CreateContentPermission]
        if not CreateContentPermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to create assignments.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Handle module creation as before

    def update(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,EditContentPermission]

        if not EditContentPermission().has_object_permission(request, self, self.get_object()):
            return Response({'detail': 'You do not have permission to update this assignment.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

        # Handle module update as before

    def list(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,ListContentPermission]
        if not ListContentPermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to list assignments.'}, status=status.HTTP_403_FORBIDDEN)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,DeleteContentPermission]
        if not DeleteContentPermission().has_object_permission(request, self, self.get_object()):
                return Response({'detail': 'You do not have permission to delete this assignment.'}, status=status.HTTP_403_FORBIDDEN)
        
        return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# class AssignmentViewSet(viewsets.ModelViewSet):
#     queryset = Assignment.objects.all()
#     serializer_class = AssignmentSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

#     def create(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to create assignments.'}, status=status.HTTP_403_FORBIDDEN)
            
#             serializer = AssignmentSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def get_queryset(self):
#         user = self.request.user

#         # Example: Filter queryset based on user's role
#         if user.role.role in ['admin','instructor','learner']:
#             return Assignment.objects.all()
#         # else:
#         #     # Filter queryset for non-admin users
#         #     return Assignment.objects.filter(user=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         if not queryset.exists():
#             # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
#             return Response([], status=status.HTTP_404_NOT_FOUND)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#         # Override the update method to check permissions
#     def update(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to update assignments.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return super().update(request, *args, **kwargs)
        

#     def destroy(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to delete assignments.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# class Assignment_SubmissionViewSet(viewsets.ModelViewSet):
#     queryset = Assignment_Submission.objects.all()
#     serializer_class = Assignment_SubmissionSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

#     def create(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to create assignment_submissions.'}, status=status.HTTP_403_FORBIDDEN)
            
#             serializer = Assignment_SubmissionSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def get_queryset(self):
#         user = self.request.user

#         # Example: Filter queryset based on user's role
#         if user.role.role == 'admin':
#             return Assignment_Submission.objects.all()
#         else:
#             # Filter queryset for non-admin users
#             return Assignment_Submission.objects.filter(user=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         if not queryset.exists():
#             # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
#                 return Response([], status=status.HTTP_404_NOT_FOUND)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#         # Override the update method to check permissions
#     def update(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to update assignment_submissions.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return super().update(request, *args, **kwargs)        

#     def destroy(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to delete assignment_submissions.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)    

class Assignment_SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Assignment_Submission.objects.all()
    serializer_class = Assignment_SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return Assignment_SubmissionCreateSerializer
        return Assignment_SubmissionSerializer

    def create(self, request, *args, **kwargs):
        if request.user.role.role not in ['admin','learner']:
            return Response({'detail': 'You do not have permission to create assignment_submissions.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        user = self.request.user

        # Example: Filter queryset based on user's role
        if user.role.role in ['admin','instructor','learner']:
            return Assignment_Submission.objects.all()
        # else:
        #     # Filter queryset for non-admin users
        #     return Assignment_Submission.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
                return Response([], status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

        # Override the update method to check permissions
    def update(self, request, *args, **kwargs):
            # Check if the requesting user has an 'admin' role
            if request.user.role.role not in ['admin','learner']:
                return Response({'detail': 'You do not have permission to update assignment_submissions.'}, status=status.HTTP_403_FORBIDDEN)
            
            return super().update(request, *args, **kwargs)        

    def destroy(self, request, *args, **kwargs):
            # Check if the requesting user has an 'admin' role
            if request.user.role.role != 'admin':
                return Response({'detail': 'You do not have permission to delete assignment_submissions.'}, status=status.HTTP_403_FORBIDDEN)
            
            return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# class Assignment_Partners_GroupViewSet(viewsets.ModelViewSet):
#     queryset = Assignment_Submission.objects.all()
#     serializer_class = Assignment_SubmissionSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_serializer_class(self):
#         if self.action == 'create':
#             return Assignment_SubmissionCreateSerializer
#         return Assignment_SubmissionSerializer

#     def create(self, request, *args, **kwargs):
#         if request.user.role.role not in ['admin','Instructor']:
#             return Response({'detail': 'You do not have permission to create assignment_submissions.'}, status=status.HTTP_403_FORBIDDEN)

#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def get_queryset(self):
#         user = self.request.user

#         # Example: Filter queryset based on user's role
#         if user.role.role in ['admin','Instructor','learner']:
#             return Assignment_Submission.objects.all()
#         # else:
#         #     # Filter queryset for non-admin users
#         #     return Assignment_Submission.objects.filter(user=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         if not queryset.exists():
#             # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
#                 return Response([], status=status.HTTP_404_NOT_FOUND)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#         # Override the update method to check permissions
#     def update(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','Instructor']:
#                 return Response({'detail': 'You do not have permission to update assignment_submissions.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return super().update(request, *args, **kwargs)        

#     def destroy(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to delete assignment_submissions.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# class Assignment_Partners_GroupViewSet(viewsets.ModelViewSet):
#     queryset = Assignment_Partners_Group.objects.all()
#     serializer_class = Assignment_Partners_GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

#     def create(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to create assignment_partners_group.'}, status=status.HTTP_403_FORBIDDEN)
            
#             serializer = Assignment_Partners_GroupSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def get_queryset(self):
#         user = self.request.user

#         # Example: Filter queryset based on user's role
#         if user.role.role == 'admin':
#             return Assignment_Partners_Group.objects.all()
#         else:
#             # Filter queryset for non-admin users
#             return Assignment_Partners_Group.objects.filter(user=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         if not queryset.exists():
#             # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
#             return Response([], status=status.HTTP_404_NOT_FOUND)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#         # Override the update method to check permissions
#     def update(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to update assignment_partners_group.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return super().update(request, *args, **kwargs)
        

#     def destroy(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to delete assignment_partners_group.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class Assignment_PartnersViewSet(viewsets.ModelViewSet):
    queryset = Assignment_Partners.objects.all()
    serializer_class = Assignment_PartnersSerializer
    permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations
    def create(self, request, *args, **kwargs):
            # Check if the requesting user has an 'admin' role
            if request.user.role.role != 'admin':
                return Response({'detail': 'You do not have permission to create assignment_partners.'}, status=status.HTTP_403_FORBIDDEN)
            serializer = Assignment_PartnersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get_queryset(self):
        user = self.request.user
        # Example: Filter queryset based on user's role
        if user.role.role == 'admin':
            return Assignment_Partners.objects.all()
        else:
            # Filter queryset for non-admin users
            return Assignment_Partners.objects.filter(user=user)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
            return Response([], status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        # Override the update method to check permissions
    def update(self, request, *args, **kwargs):
            # Check if the requesting user has an 'admin' role
            if request.user.role.role != 'admin':
                return Response({'detail': 'You do not have permission to update assignment_partners.'}, status=status.HTTP_403_FORBIDDEN)
            return super().update(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
            # Check if the requesting user has an 'admin' role
            if request.user.role.role != 'admin':
                return Response({'detail': 'You do not have permission to delete assignment_partners.'}, status=status.HTTP_403_FORBIDDEN)
            return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)        

class Assignment_GradingViewSet(viewsets.ModelViewSet):
    queryset = Assignment_Grading.objects.all()
    serializer_class = Assignment_GradingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,CreateGradingPermission]
        if not CreateGradingPermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to create gradings.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = Assignment_GradingSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Handle module creation as before

    def update(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,EditGradingPermission]

        if not EditGradingPermission().has_object_permission(request, self, self.get_object()):
            return Response({'detail': 'You do not have permission to update this grading.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

        # Handle module update as before

    def list(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,ListGradingPermission]
        if not ListGradingPermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to list gradings.'}, status=status.HTTP_403_FORBIDDEN)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,DeleteGradingPermission]
        if not DeleteGradingPermission().has_object_permission(request, self, self.get_object()):
                return Response({'detail': 'You do not have permission to delete this grading.'}, status=status.HTTP_403_FORBIDDEN)
        
        return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# class EnrollmentViewSet(viewsets.ModelViewSet):
#     queryset = Enrollment.objects.all()
#     serializer_class = EnrollmentSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

#     def create(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to create enrollments.'}, status=status.HTTP_403_FORBIDDEN)
            
#             serializer = EnrollmentSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def get_queryset(self):
#         user = self.request.user

#         # Example: Filter queryset based on user's role
#         if user.role.role in ['admin','instructor','learner']:
#             return Enrollment.objects.all()
#         # else:
#         #     # Filter queryset for non-admin users
#         #     return Enrollment.objects.filter(user=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         if not queryset.exists():
#             # return Response({'detail': 'No objects found'}, status=status.HTTP_404_NOT_FOUND)
#             return Response([], status=status.HTTP_404_NOT_FOUND)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#         # Override the update method to check permissions
#     def update(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role not in ['admin','instructor']:
#                 return Response({'detail': 'You do not have permission to update enrollments.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return super().update(request, *args, **kwargs)
        

#     def destroy(self, request, *args, **kwargs):
#             # Check if the requesting user has an 'admin' role
#             if request.user.role.role != 'admin':
#                 return Response({'detail': 'You do not have permission to delete enrollments.'}, status=status.HTTP_403_FORBIDDEN)
            
#             return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,CreatePermission]
        if not CreatePermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to create enrollment.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Handle module creation as before

    def update(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,EditPermission]

        if not EditPermission().has_object_permission(request, self, self.get_object()):
            return Response({'detail': 'You do not have permission to update this enrollment.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

        # Handle module update as before

    def list(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,ListPermission]
        if not ListPermission().has_permission(request, self):
                return Response({'detail': 'You do not have permission to list enrollment.'}, status=status.HTTP_403_FORBIDDEN)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated,DeletePermission]
        if not DeletePermission().has_object_permission(request, self, self.get_object()):
                return Response({'detail': 'You do not have permission to delete this enrollment.'}, status=status.HTTP_403_FORBIDDEN)
        
        return Response({'detail': 'Delete operation is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class CourseByCategoryListView(generics.RetrieveAPIView):
    queryset = Category.objects.all()  # Assuming you have an Author model
    serializer_class = CourseSerializer
    lookup_url_kwarg = 'category_id'
    permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

    def get(self, request, *args, **kwargs):
        if request.user.role.role not in ['admin','instructor','learner']:
                return Response({'detail': 'You do not have permission.'}, status=status.HTTP_403_FORBIDDEN)
        category_id = self.kwargs.get('category_id')

        try:
            category = Category.objects.get(id=category_id)
            course = Course.objects.filter(category=category)
            
            if course.exists():
                serializer = self.get_serializer(course, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # return Response({'detail': 'No course found for this category.'}, status=status.HTTP_404_NOT_FOUND)
                return Response([], status=status.HTTP_404_NOT_FOUND)

        
        except Category.DoesNotExist:
            return Response({'detail': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)
        

class ModuleByCourseListView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = ModuleSerializer
    lookup_url_kwarg = 'course_id'
    permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

    def get(self, request, *args, **kwargs):

        if request.user.role.role not in ['admin','instructor','learner']:
            return Response({'detail': 'You do not have permission.'}, status=status.HTTP_403_FORBIDDEN)

        course_id = self.kwargs.get('course_id')

        try:
            course = Course.objects.get(id=course_id)
            module = Module.objects.filter(course=course)
            
            if module.exists():
                serializer = self.get_serializer(module, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # return Response({'detail': 'No module found for this course.'}, status=status.HTTP_404_NOT_FOUND)
                #  return Response({'detail': 'No module found for this course.'}, status=status.HTTP_404_NOT_FOUND)
                return Response([], status=status.HTTP_404_NOT_FOUND)
            
        
        except Course.DoesNotExist:
            return Response({'detail': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)
        
class UnitByModuleListView(generics.RetrieveAPIView):
    queryset = Module.objects.all()  # Assuming you have an Author model
    serializer_class = UnitSerializer
    lookup_url_kwarg = 'module_id'
    permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations


    def get(self, request, *args, **kwargs):

        if request.user.role.role not in ['admin','instructor','learner']:
            return Response({'detail': 'You do not have permission.'}, status=status.HTTP_403_FORBIDDEN)

        module_id = self.kwargs.get('module_id')

        try:
            module = Module.objects.get(id=module_id)
            unit = Unit.objects.filter(module=module)
            
            if unit.exists():
                serializer = self.get_serializer(unit, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # return Response({'detail': 'No unit found for this module.'}, status=status.HTTP_404_NOT_FOUND)
                return Response([], status=status.HTTP_404_NOT_FOUND)
        
        except Module.DoesNotExist:
            return Response({'detail': 'Module not found.'}, status=status.HTTP_404_NOT_FOUND)
        

class VideoByUnitListView(generics.RetrieveAPIView):
    queryset = Unit.objects.all()  # Assuming you have an Author model
    serializer_class = VideoSerializer
    lookup_url_kwarg = 'unit_id'
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        if request.user.role.role not in ['admin','instructor','learner']:
            return Response({'detail': 'You do not have permission.'}, status=status.HTTP_403_FORBIDDEN)

        unit_id = self.kwargs.get('unit_id')


        try:
            unit = Unit.objects.get(id=unit_id)
            video = Video.objects.filter(unit=unit)
            
            if video.exists():
                serializer = self.get_serializer(video, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'No video found for this unit.'}, status=status.HTTP_404_NOT_FOUND)
        
        except Unit.DoesNotExist:
            return Response({'detail': 'Unit not found.'}, status=status.HTTP_404_NOT_FOUND)

class FileByUnitListView(generics.RetrieveAPIView):
    queryset = Unit.objects.all()  # Assuming you have an Author model
    serializer_class = FileSerializer
    lookup_url_kwarg = 'unit_id'
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        if request.user.role.role not in ['admin','instructor','learner']:
            return Response({'detail': 'You do not have permission to delete.'}, status=status.HTTP_403_FORBIDDEN)
                
        unit_id = self.kwargs.get('unit_id')

        try:
            unit = Unit.objects.get(id=unit_id)
            file = File.objects.filter(unit=unit)
            
            if file.exists():
                serializer = self.get_serializer(file, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # return Response({'detail': 'No files found for this unit.'}, status=status.HTTP_404_NOT_FOUND)
                return Response([], status=status.HTTP_404_NOT_FOUND)
        
        except Unit.DoesNotExist:
            return Response({'detail': 'Unit not found.'}, status=status.HTTP_404_NOT_FOUND)    


class AssignmentByUnitListView(generics.RetrieveAPIView):
    queryset = Unit.objects.all()  # Assuming you have an Author model
    serializer_class = AssignmentSerializer
    lookup_url_kwarg = 'unit_id'
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):

        if request.user.role.role not in ['admin','instructor','learner']:
            return Response({'detail': 'You do not have permission to delete.'}, status=status.HTTP_403_FORBIDDEN)
                
        unit_id = self.kwargs.get('unit_id')


        try:
            unit = Unit.objects.get(id=unit_id)
            assignment = Assignment.objects.filter(unit=unit)
            
            if assignment.exists():
                serializer = self.get_serializer(assignment, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # return Response({'detail': 'No Assignment found for this unit.'}, status=status.HTTP_404_NOT_FOUND)
                return Response([], status=status.HTTP_404_NOT_FOUND)
        
        except Unit.DoesNotExist:
            return Response({'detail': 'Unit not found.'}, status=status.HTTP_404_NOT_FOUND)  


class Assignment_SubmissionByAssignmentListView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()  # Assuming you have an Author model
    serializer_class = Assignment_SubmissionSerializer
    lookup_url_kwarg = 'assignment_id'
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request, *args, **kwargs):

        if request.user.role.role not in ['admin','instructor','learner']:
            return Response({'detail': 'You do not have permission to delete.'}, status=status.HTTP_403_FORBIDDEN)
                
        assignment_id = self.kwargs.get('assignment_id')


        try:
            assignment = Assignment.objects.get(id=assignment_id)
            assignment_submission = Assignment_Submission.objects.filter(assignment=assignment)
            
            if assignment_submission.exists():
                serializer = self.get_serializer(assignment_submission, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # return Response({'detail': 'No assignment_submissions found for this assignment.'}, status=status.HTTP_404_NOT_FOUND)
                return Response([], status=status.HTTP_404_NOT_FOUND)
        
        except Assignment.DoesNotExist:
            return Response({'detail': 'Assignment not found.'}, status=status.HTTP_404_NOT_FOUND)

# class Assignment_Partners_GroupByAssignmentListView(generics.RetrieveAPIView):
#     queryset = Assignment.objects.all()  # Assuming you have an Author model
#     serializer_class = Assignment_Partners_GroupSerializer
#     lookup_url_kwarg = 'assignment_id'
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, *args, **kwargs):

#         if request.user.role.role != 'admin':
#             return Response({'detail': 'You do not have permission to delete.'}, status=status.HTTP_403_FORBIDDEN)

#         assignment_id = self.kwargs.get('assignment_id')

#         try:
#             assignment = Assignment.objects.get(id=assignment_id)
#             assignment_partners_group = Assignment_Partners_Group.objects.filter(assignment=assignment)
            
#             if assignment_partners_group.exists():
#                 serializer = self.get_serializer(assignment_partners_group, many=True)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             else:
#                 # return Response({'detail': 'No assignment_partners found for this assignment.'}, status=status.HTTP_404_NOT_FOUND)
#                 return Response([], status=status.HTTP_404_NOT_FOUND)
        
#         except Assignment.DoesNotExist:
#             return Response({'detail': 'Assignment not found.'}, status=status.HTTP_404_NOT_FOUND)


class Assignment_PartnersByAssignmentListView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()  # Assuming you have an Author model
    serializer_class = Assignment_PartnersSerializer
    lookup_url_kwarg = 'assignment_id'
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        if request.user.role.role != 'admin':
            return Response({'detail': 'You do not have permission to delete.'}, status=status.HTTP_403_FORBIDDEN)
        assignment_id = self.kwargs.get('assignment_id')
        try:
            assignment = Assignment.objects.get(id=assignment_id)
            assignment_partners = Assignment_Partners.objects.filter(assignment=assignment)
            if assignment_partners.exists():
                serializer = self.get_serializer(assignment_partners, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # return Response({'detail': 'No assignment_partners found for this assignment.'}, status=status.HTTP_404_NOT_FOUND)
                return Response([], status=status.HTTP_404_NOT_FOUND)
        except Assignment.DoesNotExist:
            return Response({'detail': 'Assignment not found.'}, status=status.HTTP_404_NOT_FOUND)


class Assignment_GradingByAssignment_SubmissionListView(generics.RetrieveAPIView):
    queryset = Assignment_Submission.objects.all()  # Assuming you have an Author model
    serializer_class = Assignment_GradingSerializer
    lookup_url_kwarg = 'assignment_submission_id'
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        if request.user.role.role not in ['admin','instructor','learner']:
            return Response({'detail': 'You do not have permission to delete.'}, status=status.HTTP_403_FORBIDDEN)
                
        assignment_submission_id = self.kwargs.get('assignment_submission_id')


        try:
            assignment_submission = Assignment_Submission.objects.get(id=assignment_submission_id)
            assignment_grading = Assignment_Grading.objects.filter(assignment_submission=assignment_submission)
            
            if assignment_grading.exists():
                serializer = self.get_serializer(assignment_grading, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # return Response({'detail': 'No assignment_grading found for this assignment_submission.'}, status=status.HTTP_404_NOT_FOUND)
                return Response([], status=status.HTTP_404_NOT_FOUND)
        
        except Assignment_Submission.DoesNotExist:
            return Response({'detail': 'Assignment_Submission not found.'}, status=status.HTTP_404_NOT_FOUND)

class EnrollmentByCourseListView(generics.RetrieveAPIView):
    queryset = Course.objects.all()  # Assuming you have an Author model
    serializer_class = EnrollmentSerializer
    lookup_url_kwarg = 'course_id'
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        if request.user.role.role not in ['admin','instructor','learner']:
            return Response({'detail': 'You do not have permission to delete.'}, status=status.HTTP_403_FORBIDDEN)
        
        course_id = self.kwargs.get('course_id')


        try:
            course = Course.objects.get(id=course_id)
            enrollment = Enrollment.objects.filter(course=course)
            
            if enrollment.exists():
                serializer = self.get_serializer(enrollment, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # return Response({'detail': 'No enrollment found for this course.'}, status=status.HTTP_404_NOT_FOUND)
                return Response([], status=status.HTTP_404_NOT_FOUND)
        
        except Course.DoesNotExist:
            return Response({'detail': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)
        

class SubCategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        parent_category_id = self.kwargs['category_id']
        parent_category = get_object_or_404(Category, id=parent_category_id)
        return Category.objects.filter(parent=parent_category)

    def list(self, request, *args, **kwargs):
        if request.user.role.role not in ['admin','instructor']:
            return Response({'detail': 'You do not have permission to access this resource.'}, status=status.HTTP_403_FORBIDDEN)

        queryset = self.get_queryset()

        if not queryset.exists():
            return Response({'detail': 'No sub_categories found for this parent category.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class Assignment_StatusView(generics.RetrieveAPIView):
#     queryset = Assignment_Status.objects.all()
#     serializer_class = Assignment_StatusSerializer

#     def get(self, request, *args, **kwargs):
#         status_param = request.query_params.get('status')
#         if status_param not in ('pass', 'fail', 'pending'):
#             return Response({"error": "Invalid status parameter"}, status=status.HTTP_400_BAD_REQUEST)

#         status = Assignment_Submission.objects.filter(
#             assignment_status__status=status_param
#         )

#         serializer = Assignment_StatusSerializer(status, many=True)
#         return Response(serializer.data)



# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import Assignment_Submission, Assignment_Status
# from .serializers import Assignment_SubmissionSerializer, Assignment_StatusSerializer

# class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
#     queryset = Assignment_Submission.objects.all()
#     serializer_class = Assignment_SubmissionSerializer

#     @action(detail=False, methods=['GET'])
#     def filter_by_status(self, request):
#         status_param = request.query_params.get('status')

#         if status_param not in ('pass', 'fail', 'pending'):
#             return Response({"error": "Invalid status parameter"}, status=status.HTTP_400_BAD_REQUEST)

#         if status_param == 'pass':
#             submissions = Assignment_Submission.objects.filter(assignment_status__status='pass')
#         elif status_param == 'fail':
#             submissions = Assignment_Submission.objects.filter(assignment_status__status='fail')
#         elif status_param == 'pending':
#             submissions = Assignment_Submission.objects.filter(assignment_status__status='pending')
#         else:
#             # When the status parameter is not in ('pass', 'fail', 'pending'), return all submissions
#             submissions = Assignment_Submission.objects.all()

#         serializer = Assignment_SubmissionSerializer(submissions, many=True)
#         return Response(serializer.data)

# class AssignmentGradingViewSet(viewsets.ModelViewSet):
#     queryset = Assignment_Grading.objects.all()
#     serializer_class = Assignment_GradingSerializer

#     # Custom action to filter assignments based on status
#     @action(detail=False, methods=['GET'])
#     def filter_by_status(self, request):
#         status_param = request.query_params.get('status')

#         if status_param not in ('pass', 'fail', 'pending'):
#             return Response({"error": "Invalid status parameter"}, status=status.HTTP_400_BAD_REQUEST)

#         if status_param == 'none':
#             submissions = Assignment_Grading.objects.all()
#         else:
#             submissions = Assignment_Grading.objects.filter(status=status_param)

#         serializer = Assignment_GradingSerializer(submissions, many=True)
#         return Response(serializer.data)


# class AssignmentStatusViewSet(viewsets.ModelViewSet):
#     queryset = Assignment_Grading.objects.all()
#     serializer_class = Assignment_GradingSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations

#     # Custom action to filter assignments based on status
#     @action(detail=False, methods=['GET'])
#     def filter_by_status(self, request):
#         status_param = request.query_params.get('status')

#         if status_param not in ('pass', 'fail', 'pending', 'none'):
#             return Response({"error": "Invalid status parameter"}, status=status.HTTP_400_BAD_REQUEST)

#         if request.user.role.role != 'admin':
#             return Response({'detail': 'You do not have permission to access this resource.'}, status=status.HTTP_403_FORBIDDEN)

#         if status_param == 'none':
#             submissions = Assignment_Grading.objects.all()
#         else:
#             submissions = Assignment_Grading.objects.filter(status=status_param)

#         serializer = Assignment_GradingSerializer(submissions, many=True)
#         return Response(serializer.data)
    


class FilterViewSet(viewsets.ModelViewSet):
    queryset = Assignment_Grading.objects.all()
    serializer_class = Assignment_GradingSerializer
    permission_classes = [permissions.IsAuthenticated]  # Apply authentication to all operations


    @action(detail=False, methods=['GET'])
    def filter_related_objects(self, request):
        status = request.query_params.get('status', None)
        grading_filter = {}

        if request.user.role.role not in ['admin','instructor','learner']:
            return Response({'detail': 'You do not have permission to access this resource.'}, status=status.HTTP_403_FORBIDDEN)

        if status is not None:
            if status == "none":
                # If status is "none," return all objects without filtering
                graded_assignments = Assignment_Grading.objects.all()
            else:
                grading_filter['status'] = status
                graded_assignments = Assignment_Grading.objects.filter(**grading_filter)
        else:
            # If status parameter is not provided, return all objects without filtering
            graded_assignments = Assignment_Grading.objects.all()

        related_submissions = graded_assignments.values_list('assignment_submission', flat=True)
        related_assignments = Assignment_Submission.objects.filter(id__in=related_submissions).values_list('assignment', flat=True)

        grading_serializer = Assignment_GradingSerializer(graded_assignments, many=True)
        submission_serializer = Assignment_SubmissionSerializer(Assignment_Submission.objects.filter(id__in=related_submissions), many=True)
        assignment_serializer = AssignmentSerializer(Assignment.objects.filter(id__in=related_assignments), many=True)

        return Response({
            'assignment_grading': grading_serializer.data,
            'assignment_submission': submission_serializer.data,
            'assignment': assignment_serializer.data
        })
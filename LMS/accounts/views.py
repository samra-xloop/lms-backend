from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Role
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from .serializers import UserWithRoleSerializer,DeletedUserSerializer
import secrets
from django.utils import timezone




#To Register New User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_user(request):
    if request.method == 'POST':
        # Check if the requesting user has an 'admin' role
        if request.user.role.role == 'admin':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                # Set username to None explicitly
                serializer.validated_data['username'] = None
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'You do not have permission to register users.'}, status=status.HTTP_403_FORBIDDEN)

    
#Login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

#To Login
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('email')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user and not user.is_deleted:  # Check if user is not deleted
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials or user is deleted'}, status=status.HTTP_401_UNAUTHORIZED)

    
#To Logout
from rest_framework.decorators import api_view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        

# For admin to assign roles to users.
from rest_framework.decorators import api_view, permission_classes
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_role(request):
    if request.method == 'POST':
        # Check if the requesting user has an 'admin' role
        if request.user.role.role == 'admin':
            email = request.data.get('email')
            role = request.data.get('role')
            
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            role_instance, created = Role.objects.get_or_create(user=user)
            role_instance.role = role
            role_instance.save()

            return Response({'message': f'Role {role} assigned to {user.email}'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'You do not have permission to assign roles.'}, status=status.HTTP_403_FORBIDDEN)




from .permissions import IsAdminUser, IsInstructorUser, IsLearnerUser
#For admin to see all active users(not deleted)
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def list_all_users(request):
    all_users = CustomUser.objects.filter(is_deleted=False)
    serializer = UserSerializer(all_users, many=True)
    return Response(serializer.data)


#For instructor to see all learners
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsInstructorUser])
def list_instructor_users(request):
    instructor = request.user
    if instructor.role.role == 'instructor':
        # Filter learners only, excluding instructors and admins
        learner_users = CustomUser.objects.filter(role__role='learner')
        serializer = UserWithRoleSerializer(learner_users, many=True)
        return Response(serializer.data)
    return Response({'detail': 'You do not have permission to access this resource.'}, status=status.HTTP_403_FORBIDDEN)

from rest_framework.decorators import api_view, permission_classes
#For learner to see their own profile
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsLearnerUser])
def list_own_user(request):
    user = CustomUser.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#For instructor to see their own profile
from rest_framework.decorators import api_view, permission_classes
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsInstructorUser])
def list_own_instructor_user(request):
    user = CustomUser.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#To update a user data
from rest_framework.decorators import api_view, permission_classes
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    if request.method == 'PUT':
        # Check if the requesting user has an 'admin' role
        if request.user.role.role == 'admin':
            email = request.data.get('email')
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response({'detail': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'You do not have permission to update users.'}, status=status.HTTP_403_FORBIDDEN)


#To delete a user
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    if request.method == 'DELETE':
        # Check if the requesting user has an 'admin' role
        if request.user.role.role == 'admin':
            email = request.data.get('email')
            try:
                user = CustomUser.objects.get(email=email)
                user.is_deleted = True
                user.save()
                return Response({'message': f'User {email} marked as deleted.'}, status=status.HTTP_204_NO_CONTENT)
            except CustomUser.DoesNotExist:
                return Response({'detail': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'detail': 'You do not have permission to delete users.'}, status=status.HTTP_403_FORBIDDEN)

#To view all deleted users
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def list_deleted_users(request):
    deleted_users = CustomUser.objects.filter(is_deleted=True)
    serializer = DeletedUserSerializer(deleted_users, many=True)
    return Response(serializer.data)


#Email Verification for password change
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PasswordResetToken
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from rest_framework.permissions import AllowAny

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def request_password_reset(request):
    try:
        email = request.data.get('email')
        user = User.objects.get(email=email)
        
        token = get_random_string(length=32)
        reset_token = PasswordResetToken(user=user, token=token)
        reset_token.save()

        send_mail(
            'Password Reset Request',
            f'Click the link to reset your password: http://localhost:8000/api/reset_password/{token}/',
            'noreply@example.com',
            [user.email],
            fail_silently=False,
        )

        return Response({'message': 'Password reset email sent.'})
    except User.DoesNotExist:
        return Response({'error': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def verify_password_reset_token(request, token):
    try:
        reset_token = PasswordResetToken.objects.get(token=token)
        if (timezone.now() - reset_token.created_at).days < 1:
            return Response({'message': 'Token is valid.'})
        else:
            reset_token.delete()
            return Response({'message': 'Token has expired.'})
    except PasswordResetToken.DoesNotExist:
        return Response({'message': 'Token is invalid.'})

@api_view(['POST'])
def reset_password(request, token):
    try:
        reset_token = PasswordResetToken.objects.get(token=token)
        if (timezone.now() - reset_token.created_at).days < 1:
            user = reset_token.user
            new_password = request.data.get('new_password')
            user.set_password(new_password)
            user.save()
            reset_token.delete()
            return Response({'message': 'Password reset successfully.'})
        else:
            reset_token.delete()
            return Response({'message': 'Token has expired.'})
    except PasswordResetToken.DoesNotExist:
        return Response({'message': 'Token is invalid.'})

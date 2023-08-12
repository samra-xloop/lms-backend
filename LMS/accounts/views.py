from django.shortcuts import render

# accounts/views.py

#Register
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
"""
@api_view(['POST'])
#def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
    
#Login 
# accounts/views.py

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import CustomUser

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

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    
#Logout
# accounts/views.py

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

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
        
        
# accounts/views.py

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_role(request):
    if request.method == 'POST':
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



# accounts/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser, Role
from .serializers import UserWithRoleSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_users_with_roles(request):
    users_with_roles = CustomUser.objects.prefetch_related('role').all()
    serializer = UserWithRoleSerializer(users_with_roles, many=True)
    return Response(serializer.data)


# accounts/views.py

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_one_users(request):
    all_users = CustomUser.objects.all()
    serializer = UserSerializer(all_users, many=True)
    return Response(serializer.data)



from .permissions import IsAdminUser

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def list_all_users(request):
    all_users = CustomUser.objects.all()
    serializer = UserSerializer(all_users, many=True)
    return Response(serializer.data)
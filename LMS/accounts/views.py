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
from .serializers import RegisterUserWithRoleSerializer,ListUserSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_user_with_role(request):
    if request.method == 'POST':
        # Check if the requesting user has an 'admin' role
        if request.user.role.role == 'admin':
            serializer = RegisterUserWithRoleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'You do not have permission to register users.'}, status=status.HTTP_403_FORBIDDEN)


    
#To Login

from django.http import JsonResponse

# User Login API
# User Login API
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

        if user and user.check_password(password):  # Check the password using check_password method
            token, _ = Token.objects.get_or_create(user=user)
            try:
                role = user.role.role
            except ObjectDoesNotExist:
                role = None
                
                
            return Response({'token': token.key,
                             'id':user.id,
                             'first_name': user.first_name,
                             'last_name': user.last_name,
                             'role': role,}, 
                            status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


    
    
#To Logout
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

from .permissions import IsAdminUser, IsInstructorUser, IsLearnerUser
#For admin to see all active users(not deleted)
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def list_all_users(request):
    all_users = CustomUser.objects.filter(is_deleted=False)
    serializer = ListUserSerializer(all_users, many=True)
    return Response(serializer.data)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import UserSerializer,UpdateUserWithRoleSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def list_single_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id, is_deleted=False)
    serializer = UserSerializer(user)
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

#For learner to see their own profile
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsLearnerUser])
def list_own_user(request):
    user = CustomUser.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#For instructor to see their own profile

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsInstructorUser])
def list_own_instructor_user(request):
    user = CustomUser.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#To update a user data
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    if request.method == 'PUT':
        # Check if the requesting user has an 'admin' role
        if request.user.role.role == 'admin':
            email = request.data.get('email')
            try:
                user = CustomUser.objects.get(email=email)
                
                # Check if the user is marked as deleted
                if user.is_deleted:
                    return Response({'detail': 'User is marked as deleted and cannot be updated.'}, status=status.HTTP_400_BAD_REQUEST)
                
                # Update the user and role using the UpdateUserWithRoleSerializer
                serializer = UpdateUserWithRoleSerializer(user, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except CustomUser.DoesNotExist:
                return Response({'detail': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
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
@permission_classes([IsAuthenticated])
def list_deleted_users(request):
    if request.user.role.role == 'admin':
        deleted_users = CustomUser.objects.filter(is_deleted=True)
        serializer = DeletedUserSerializer(deleted_users, many=True)
        return Response(serializer.data)


#Email Verification for password change
from .models import PasswordResetToken
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from rest_framework.permissions import AllowAny
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
            f'Click the link to reset your password: http://localhost:8000/reset_password/{token}/',
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
            
            # Set the user's new password
            user.set_password(new_password)
            user.save()
            
            reset_token.delete()
            return Response({'message': 'Password reset successfully.'})
        else:
            reset_token.delete()
            return Response({'message': 'Token has expired.'})
    except PasswordResetToken.DoesNotExist:
        return Response({'message': 'Token is invalid.'})



# Teams 
from .models import Team
from .serializers import TeamSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_team(request):
    if request.method == 'POST':
        # Check if the requesting user has an 'admin' role
        if request.user.role.role == 'admin':
            team_name = request.data.get('name')  # Extract the team name from the JSON data
            description = request.data.get('description')  # Extract the team description
            
            # Check if a team with the same name already exists
            if Team.objects.filter(name=team_name).exists():
                return Response({'detail': 'A team with this name already exists.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Get the name of the user who created the team
            created_by = request.user.get_full_name()
            
            # Create a new team with the provided data
            team = Team(name=team_name, description=description, created_by=created_by)
            team.save()

            # Serialize the team object to include in the response
            serialized_team = TeamSerializer(team)

            return Response(serialized_team.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'You do not have permission to create teams.'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_team(request):
    if request.method == 'DELETE':
        # Check if the requesting user has an 'admin' role
        if request.user.role.role == 'admin':
            team_id = request.data.get('team_id')
            try:
                team = Team.objects.get(pk=team_id)
                team.is_deleted = True
                team.save()
                return Response({'message': f'Team {team.name} marked as deleted.'}, status=status.HTTP_204_NO_CONTENT)
            except Team.DoesNotExist:
                return Response({'detail': 'Team does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'detail': 'You do not have permission to delete teams.'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_deleted_teams(request):
    if request.user.role.role == 'admin':
        deleted_teams = Team.objects.filter(is_deleted=True)
        serializer = TeamSerializer(deleted_teams, many=True)
        return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_users_to_team(request):
    if request.method == 'POST':
        # Check if the requesting user has an 'admin' role
        if request.user.role.role == 'admin':
            team_name = request.data.get('team_name')
            user_ids = request.data.get('user_ids')  # Expect a list of user IDs


            try:
                team = Team.objects.get(name=team_name)
            except Team.DoesNotExist:
                return Response({'detail': 'Team not found.'}, status=status.HTTP_404_NOT_FOUND)

            if team.is_deleted:
                return Response({'detail': 'Team is deleted and cannot accept users.'}, status=status.HTTP_400_BAD_REQUEST)

            added_users = []
            not_found_users = []
            not_found_or_deleted_users = []

            for user_id in user_ids:
                try:
                    user = CustomUser.objects.get(id=user_id)
                    if user.is_deleted:
                        not_found_or_deleted_users.append(user_id)
                    else:
                        team.users.add(user)
                        user.teams.add(team)  # Add the team to the user
                        added_users.append(user_id)
                except CustomUser.DoesNotExist:
                    not_found_or_deleted_users.append(user_id)


            response_data = {
                'added_users': added_users,
                'not_found_users': not_found_users,
                'not_found_or_deleted_users': not_found_or_deleted_users,
                'detail': 'Users added to the team successfully.',
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'You do not have permission to add users to teams.'}, status=status.HTTP_403_FORBIDDEN)


from .serializers import CustomUserSerializer  
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_teams_data(request):
    if request.method == 'GET':
        # Retrieve teams where `is_deleted` is False and serialize the data
        teams = Team.objects.filter(is_deleted=False)
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



from course.models import Course # Import the Courses model
@api_view(['POST'])
def add_courses_to_team(request):
    if request.method == 'POST':
        team_id = request.data.get('team_id')
        course_ids = request.data.get('course_ids', [])

        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({'detail': 'Team not found'}, status=status.HTTP_404_NOT_FOUND)

        for course_id in course_ids:
            try:
                course = Course.objects.get(pk=course_id)
                team.courses.add(course)
            except Course.DoesNotExist:
                return Response({'detail': f'Course with ID {course_id} not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'detail': 'Courses added to the team successfully'}, status=status.HTTP_200_OK)



from django.contrib.auth import get_user_model
@api_view(['POST'])
def assign_course_to_users(request):
    if request.method == 'POST':
        user_ids = request.data.get('user_ids', [])
        course_name = request.data.get('course_name')

        course = Course.objects.filter(title=course_name).first()
        if course is None:
            return Response({'detail': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        assigned_users = []
        not_found_users = []

        for user_id in user_ids:
            try:
                user = get_user_model().objects.get(id=user_id)
                user.courses.add(course)
                assigned_users.append(user_id)
            except get_user_model().DoesNotExist:
                not_found_users.append(user_id)

        response_data = {
            'assigned_users': assigned_users,
            'not_found_users': not_found_users,
            'detail': f'Course "{course_name}" assigned to users',
        }

        return Response(response_data, status=status.HTTP_200_OK)

#Remove Users from Teams
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_users_from_team(request):
    if request.method == 'POST':
        # Check if the requesting user has an 'admin' role
        if request.user.role.role == 'admin':
            team_name = request.data.get('team_name')
            user_ids = request.data.get('user_ids')  # Expect a list of user emails

            try:
                team = Team.objects.get(name=team_name)
            except Team.DoesNotExist:
                return Response({'detail': 'Team not found.'}, status=status.HTTP_404_NOT_FOUND)

            if team.is_deleted:
                return Response({'detail': 'Team is deleted and cannot remove users.'}, status=status.HTTP_400_BAD_REQUEST)

            removed_users = []
            not_found_users = []

            for user_id in user_ids:
                try:
                    user = CustomUser.objects.get(id=user_id)
                    team.users.remove(user)  # Remove the user from the team
                    user.teams.remove(team)  # Remove the team from the user
                    removed_users.append(user_id)
                except CustomUser.DoesNotExist:
                    not_found_users.append(user_id)

            response_data = {
                'removed_users': removed_users,
                'not_found_users': not_found_users,
                'detail': 'Users removed from the team successfully.',
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'You do not have permission to remove users from teams.'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_courses_from_team(request):
    if request.method == 'POST':
        team_id = request.data.get('team_id')
        course_ids = request.data.get('course_ids', [])

        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({'detail': 'Team not found'}, status=status.HTTP_404_NOT_FOUND)

        removed_courses = []
        not_found_courses = []

        for course_id in course_ids:
            try:
                course = Course.objects.get(pk=course_id)
                team.courses.remove(course)  # Remove the course from the team
                removed_courses.append(course_id)
            except Course.DoesNotExist:
                not_found_courses.append(course_id)

        return Response({'removed_courses': removed_courses, 'not_found_courses': not_found_courses, 'detail': 'Courses removed from the team successfully'}, status=status.HTTP_200_OK)



@api_view(['POST'])
def remove_courses_from_users(request):
    if request.method == 'POST':
        email_list = request.data.get('email_list', [])
        course_name = request.data.get('course_name')

        course = Course.objects.filter(name=course_name).first()
        if course is None:
            return Response({'detail': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        removed_users = []
        not_found_users = []

        for email in email_list:
            try:
                user = get_user_model().objects.get(email=email)
                user.courses.remove(course)  # Remove the course from the user
                removed_users.append(email)
            except get_user_model().DoesNotExist:
                not_found_users.append(email)

        response_data = {
            'removed_users': removed_users,
            'not_found_users': not_found_users,
            'detail': f'Course "{course_name}" removed from users',
        }

        return Response(response_data, status=status.HTTP_200_OK)


"""
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
            
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_users_to_team(request):
    if request.method == 'POST':
        # Check if the requesting user has an 'admin' role
        if request.user.role.role == 'admin':
            team_name = request.data.get('team_name')
            user_ids = request.data.get('user_ids')  # Expect a list of user emails

            try:
                team = Team.objects.get(name=team_name)
            except Team.DoesNotExist:
                return Response({'detail': 'Team not found.'}, status=status.HTTP_404_NOT_FOUND)

            if team.is_deleted:
                return Response({'detail': 'Team is deleted and cannot accept users.'}, status=status.HTTP_400_BAD_REQUEST)

            added_users = []
            not_found_users = []

            for user_id in user_ids:
                try:
                    user = CustomUser.objects.get(id=user_id)
                    team.users.add(user)
                    user.teams.add(team)  # Add the team to the user
                    added_users.append(user_id)
                except CustomUser.DoesNotExist:
                    not_found_users.append(user_id)

            response_data = {
                'added_users': added_users,
                'not_found_users': not_found_users,
                'detail': 'Users added to the team successfully.',
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'You do not have permission to add users to teams.'}, status=status.HTTP_403_FORBIDDEN)


"""
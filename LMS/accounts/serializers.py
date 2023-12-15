# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser, Role
from course.models import Course
from course.serializers import CourseSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'gender', 'city', 'country', 'phone_number', 'profile_picture', 'is_active', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            city=validated_data['city'],
            country=validated_data['country'],
            phone_number=validated_data['phone_number'],
            profile_picture=validated_data['profile_picture'],
            is_active=validated_data['is_active']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

from rest_framework import serializers
from .models import CustomUser, Role

class RegisterUserWithRoleSerializer(serializers.ModelSerializer):
    role = serializers.CharField()  # Accept role as a string field

    class Meta:
        model = CustomUser
        fields = ['id','email', 'first_name', 'last_name', 'gender', 'city', 'country', 'phone_number', 'profile_picture', 'is_active', 'password', 'role', 'avatar']

    def create(self, validated_data):
        # Extract the role from the validated data
        role_data = validated_data.pop('role')

        # Create a new user
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        # Assign the role to the user
        Role.objects.create(user=user, role=role_data)

        return user
    
#For User With Roles
class UserWithRoleSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(source='role.role')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role']  
 
 #Check Deleted Users       
class DeletedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'is_deleted']


#For Teams
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    teams = serializers.StringRelatedField(many=True)  
    courses = CourseSerializer(many=True)

    class Meta:
        model = CustomUser
        fields =['id', 'email']


        
from rest_framework import serializers
from .models import Team
from accounts.serializers import UserSerializer

class TeamWithUsersSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    

    class Meta:
        model = Team
        fields = '__all__'

    def get_users(self, obj):
        users = obj.users.filter(is_deleted=False)
        return UserSerializer(users, many=True).data

    
from rest_framework import serializers
from .models import CustomUser, Role

from rest_framework import serializers
from .models import CustomUser, Role

class UpdateUserWithRoleSerializer(serializers.ModelSerializer):
    role = serializers.CharField(required=False)  # Accept role as an optional field

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'gender', 'city', 'country', 'phone_number', 'profile_picture', 'is_active', 'password', 'role']

    def update(self, instance, validated_data):
        # Extract the role from the validated data (if present)
        role_data = validated_data.pop('role', None)

        # Update the user's fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Save the updated user
        instance.save()

        # Assign the role to the user (if role data is provided)
        if role_data:
            role, _ = Role.objects.get_or_create(user=instance)
            role.role = role_data
            role.save()

        return instance

class ListUserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(source='role.role')

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'gender', 'city', 'country', 'phone_number', 'profile_picture', 'is_active', 'created_at', 'updated_at', 'role','teams','courses']

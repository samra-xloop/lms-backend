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


#For Roles 
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['user', 'role']
        
#For User
class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(source='role.role')  

    class Meta:
        model = CustomUser
        fields = ['id','username', 'email', 'first_name', 'last_name', 'gender', 'city', 'country', 'phone_number', 'profile_picture', 'is_active', 'created_at', 'updated_at', 'role']  # Include 'role' here

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

    

# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser, Role

"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
"""
    
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





class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['user', 'role']
        
"""        
class UserWithRoleSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(source='role.role')

    class Meta:
        model = CustomUser
        fields = ['username','email', 'first_name', 'last_name', 'role']
        
        
# accounts/serializers.py

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','email', 'first_name', 'last_name', 'gender', 'city', 'country', 'phone_number', 'profile_picture', 'is_active', 'created_at', 'updated_at']
"""

# accounts/serializers.py
class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(source='role.role')  # Add this line

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'gender', 'city', 'country', 'phone_number', 'profile_picture', 'is_active', 'created_at', 'updated_at', 'role']  # Include 'role' here

class UserWithRoleSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(source='role.role')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role']  # Include 'role' here
        
class DeletedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'is_deleted']

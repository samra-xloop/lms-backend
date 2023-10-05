"""
File: models.py
Author: Muhammad Humza
Date: 09-08-2023 
Description: This module contains Django models for the accounts app.

This module defines the CustomUser model, Role model, PasswordResetToken model, and Team model.

Usage: These models are used to manage user accounts, roles, password reset tokens, and teams in the application.

"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings


    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, default=None, null=True)  # Set default to None and allow null
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    city = models.CharField(max_length=100, default='Unknown')
    country = models.CharField(max_length=100, default='Unknown')
    phone_number = models.CharField(max_length=20, default='Unknown')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    teams = models.ManyToManyField('Team', related_name='members', blank=True)
    courses = models.ManyToManyField('course.Course', related_name='courses', blank=True)

    

    def __str__(self):
        return self.username
    
    
class Role(models.Model):
        ROLE_CHOICES = [
            ('admin', 'Admin'),
            ('instructor', 'Instructor'),
            ('learner', 'Learner'),
        ]
    
        user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
        role = models.CharField(max_length=20, choices=ROLE_CHOICES)

        def __str__(self):
            return f"{self.user.email} - {self.role}"
        


class PasswordResetToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=32)
    created_at = models.DateTimeField(default=timezone.now)

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db import models
from django.utils import timezone

class Team(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank=True)  # Add a TextField for team description
    created_by = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    users = models.ManyToManyField('CustomUser', related_name='team_users', blank=True)
    courses = models.ManyToManyField('course.Course', related_name='teams', blank=True)
    


    def __str__(self):
        return self.name 
    
    




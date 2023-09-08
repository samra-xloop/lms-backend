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
from course.models import Category, Courses 

    
class CustomUser(AbstractUser):
    """
    CustomUser model represents user profiles with additional fields.

    Attributes:
        email (EmailField): User's unique email address.
        username (CharField): User's unique username (optional).
        first_name (CharField): User's first name.
        last_name (CharField): User's last name.
        gender (CharField): User's gender with choices (Male, Female, Other).
        city (CharField): User's city.
        country (CharField): User's country.
        phone_number (CharField): User's phone number.
        profile_picture (ImageField): User's profile picture (optional).
        is_active (BooleanField): Whether the user is active.
        is_deleted (BooleanField): Whether the user is deleted.
        created_at (DateTimeField): Timestamp of user creation.
        updated_at (DateTimeField): Timestamp of user last update.
        teams (ManyToManyField): User's associated teams.
        courses (ManyToManyField): User's associated courses.

    Methods:
        __str__: Returns the username as the string representation of the user.

    """
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
    courses = models.ManyToManyField('course.Courses', related_name='courses', blank=True)
    

    def __str__(self):
        return self.username
    
    
class Role(models.Model):
        """
        Role model represents user roles in the application.

        Attributes:
            ROLE_CHOICES (list): Choices for user roles (admin, instructor, learner).
            user (OneToOneField): User associated with the role.
            role (CharField): User's role (admin, instructor, learner).

        Methods:
            __str__: Returns a string representation of the user's email and role.

        """
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
    """
    PasswordResetToken model represents tokens for resetting user passwords.

    Attributes:
        user (ForeignKey): User associated with the password reset token.
        token (CharField): Reset token string.
        created_at (DateTimeField): Timestamp of token creation.

    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=32)
    created_at = models.DateTimeField(default=timezone.now)

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings
from course.models import Courses
from django.db import models
from django.utils import timezone

class Team(models.Model):
    """
    Team model represents teams in the application.

    Attributes:
        name (CharField): Team's name (unique).
        description (TextField): Team's description (optional).
        created_by (CharField): User who created the team (optional).
        created_at (DateTimeField): Timestamp of team creation.
        updated_at (DateTimeField): Timestamp of team last update.
        is_deleted (BooleanField): Whether the team is deleted.
        users (ManyToManyField): Users in the team.
        courses (ManyToManyField): Courses associated with the team.

    Methods:
        __str__: Returns the team's name as the string representation.

    """
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank=True)  # Add a TextField for team description
    created_by = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    users = models.ManyToManyField(CustomUser, related_name='team_users', blank=True)
    courses = models.ManyToManyField(Courses, related_name='teams', blank=True)
    


    def __str__(self):
        return self.name 
    
    




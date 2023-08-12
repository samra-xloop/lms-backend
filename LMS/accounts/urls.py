# accounts/urls.py
"""
from django.urls import path
from .views import register_user, user_login, user_logout

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
"""
# accounts/urls.py

from django.urls import path
from .views import register_user, user_login, user_logout,assign_role,list_users_with_roles,list_one_users,list_all_users

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('assign_role/', assign_role, name='assign_role'),
    path('list_users_with_roles/', list_users_with_roles, name='list_users_with_roles'),
    path('list_one_users/', list_one_users, name='list_one_users'),
    path('list_all_users/', list_all_users, name='list_all_users'),
]
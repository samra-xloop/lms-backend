# accounts/urls.py

from django.urls import path
from .views import user_login, user_logout,list_all_users,list_instructor_users,list_own_user,list_own_instructor_user, update_user, delete_user,register_user,assign_role,list_deleted_users,reset_password,verify_password_reset_token,request_password_reset
urlpatterns = [
    path('register/', register_user, name='register'),
    path('update_user/', update_user, name='update_user'),
    path('delete_user/', delete_user, name='delete_user'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('assign_role/', assign_role, name='assign_role'),
    path('list_all_users/', list_all_users, name='list_all_users'),
    path('list_instructor_users/', list_instructor_users, name='list_instructor_users'),
    path('list_own_user/', list_own_user, name='list_own_user'),
    path('list_own_instructor_user/', list_own_instructor_user, name='list_own_instructor_user'),
    path('list_deleted_users/', list_deleted_users, name='list_deleted_users'),
    path('request_password_reset/', request_password_reset, name='request_password_reset'),
    path('verify_password_reset_token/<str:token>/', verify_password_reset_token, name='verify_password_reset_token'),
    path('reset_password/<str:token>/', reset_password, name='reset_password'),


]
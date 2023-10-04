# accounts/urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register_user_with_role, name='register'),
    path('update_user/', views.update_user_with_role, name='update_user'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('list_all_users/', views.list_all_users, name='list_all_users'),
    path('list_instructor_users/', views.list_instructor_users, name='list_instructor_users'),
    path('list_own_user/', views.list_own_user, name='list_own_user'),
    path('list_own_instructor_user/', views.list_own_instructor_user, name='list_own_instructor_user'),
    path('list_deleted_users/', views.list_deleted_users, name='list_deleted_users'),
    path('request_password_reset/', views.request_password_reset, name='request_password_reset'),
    path('verify_password_reset_token/<str:token>/', views.verify_password_reset_token, name='verify_password_reset_token'),
    path('reset_password/<str:token>/', views.reset_password, name='reset_password'),
    path('create_team/', views.create_team, name='create_team'),
    path('delete_team/', views.delete_team, name='delete_team'),
    path('list_deleted_teams/', views.list_deleted_teams, name='list_deleted_teams'),
    path('add_users_to_team/', views.add_users_to_team, name='add_users_to_team'),
    path('teams_list_data/', views.list_teams_data, name='list_teams_data'),
    path('add_courses_to_team/', views.add_courses_to_team, name='add_courses_to_team'),
    path('assign_course_to_users/', views.assign_course_to_users, name='assign_course_to_users'),
    path('remove_users_from_team/', views.remove_users_from_team, name='remove_users_from_team'),
    path('remove_courses_from_team/', views.remove_courses_from_team, name='remove_courses_from_team'),
    path('remove_courses_from_users/', views.remove_courses_from_users, name='remove_courses_from_users'),
    path('list_single_user/<int:user_id>/', views.list_single_user, name='list_single_user'),
    


   






]
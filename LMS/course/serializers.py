from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class UnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files 
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class Quiz_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz_Question 
        fields = '__all__'

class Question_OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question_Option 
        fields = '__all__'

class Quiz_SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz_Submission 
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment 
        fields = '__all__'

class Assignment_SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment_Submission
        fields = '__all__'

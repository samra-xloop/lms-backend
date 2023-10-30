from rest_framework import serializers
from .models import *

class ConditionalDeletedAtMixin:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not instance.is_delete:
            data.pop('deleted_at', None)
        return data
    
class ConditionalUpdatedAtMixin:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not instance.is_updated:
            data.pop('updated_at', None)
        return data

class ConditionalUpdated_ByAtMixin:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not instance.is_updated:
            data.pop('updated_by', None)
        return data

class ConditionalGrading_DatetimeAtMixin:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not instance.is_graded:
            data.pop('grading_datetime', None)
        return data    

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer( ConditionalDeletedAtMixin, ConditionalUpdatedAtMixin, ConditionalUpdated_ByAtMixin ,serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

class CourseSerializer( ConditionalDeletedAtMixin, ConditionalUpdatedAtMixin, ConditionalUpdated_ByAtMixin,serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'

class ModuleSerializer( ConditionalDeletedAtMixin, ConditionalUpdatedAtMixin, ConditionalUpdated_ByAtMixin,serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = '__all__'

class UnitSerializer( ConditionalDeletedAtMixin, ConditionalUpdatedAtMixin, ConditionalUpdated_ByAtMixin,serializers.ModelSerializer):
    
    class Meta:
        model = Unit
        fields = '__all__'

class VideoSerializer( ConditionalDeletedAtMixin, ConditionalUpdatedAtMixin, ConditionalUpdated_ByAtMixin,serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = '__all__'

class FileSerializer( ConditionalDeletedAtMixin, ConditionalUpdatedAtMixin, ConditionalUpdated_ByAtMixin,serializers.ModelSerializer):
    
    class Meta:
        model = File 
        fields = '__all__'

# class QuizSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Quiz
#         fields = '__all__'

# class Quiz_QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Quiz_Question 
#         fields = '__all__'

# class Question_OptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question_Option 
#         fields = '__all__'

# class Quiz_SubmissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Quiz_Submission 
#         fields = '__all__'

class AssignmentSerializer(ConditionalDeletedAtMixin, ConditionalUpdatedAtMixin, ConditionalUpdated_ByAtMixin,serializers.ModelSerializer):
    
    class Meta:
        model = Assignment 
        fields = '__all__'

# class Assignment_SubmissionSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Assignment_Submission
#         fields = '__all__'

class Assignment_GradingSerializer(ConditionalGrading_DatetimeAtMixin,serializers.ModelSerializer):
    class Meta:
        model = Assignment_Grading
        fields = '__all__'

class Assignment_SubmissionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment_Submission
        fields = '__all__'

    def create(self, validated_data):
        # Create the Assignment_Submission instance
        assignment_submission = Assignment_Submission.objects.create(**validated_data)

        # Create an Assignment_Grading instance related to the submission with default values
        grading_instance = Assignment_Grading.objects.create(
            assignment_submission=assignment_submission,
            assignment=assignment_submission.assignment
            # Set default values here
        )

        return assignment_submission

class Assignment_SubmissionSerializer(serializers.ModelSerializer):
    grading = Assignment_GradingSerializer(read_only=True)  # Serializer for the related Assignment_Grading instance

    class Meta:
        model = Assignment_Submission
        fields = '__all__'

class Assignment_Partners_GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment_Partners_Group
        fields = '__all__'

class Assignment_PartnersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment_Partners
        fields = '__all__'
        # fields = ['id']

# class Assignment_GradingSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Assignment_Grading
#         fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = '__all__'

# class Assignment_StatusSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Assignment_Status
#         fields = '__all__'


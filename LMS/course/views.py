from course.models import *
from .serializers import *
from rest_framework import viewsets
from django.contrib.auth.models import User


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer    

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer    

class Quiz_QuestionViewSet(viewsets.ModelViewSet):
    queryset = Quiz_Question.objects.all()
    serializer_class = Quiz_QuestionSerializer    

class Question_OptionViewSet(viewsets.ModelViewSet):
    queryset = Question_Option.objects.all()
    serializer_class = Question_OptionSerializer    

class Quiz_SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Quiz_Submission.objects.all()
    serializer_class = Quiz_SubmissionSerializer    

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class Assignment_SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Assignment_Submission.objects.all()
    serializer_class = Assignment_SubmissionSerializer

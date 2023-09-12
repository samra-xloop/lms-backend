from course.models import *
from .serializers import *
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.response import Response


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer    

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

# class QuizViewSet(viewsets.ModelViewSet):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer    

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

# class Quiz_QuestionViewSet(viewsets.ModelViewSet):
#     queryset = Quiz_Question.objects.all()
#     serializer_class = Quiz_QuestionSerializer    

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

# class Question_OptionViewSet(viewsets.ModelViewSet):
#     queryset = Question_Option.objects.all()
#     serializer_class = Question_OptionSerializer    

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

# class Quiz_SubmissionViewSet(viewsets.ModelViewSet):
#     queryset = Quiz_Submission.objects.all()
#     serializer_class = Quiz_SubmissionSerializer    

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

class Assignment_SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Assignment_Submission.objects.all()
    serializer_class = Assignment_SubmissionSerializer


    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

class Assignment_SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Assignment_Submission.objects.all()
    serializer_class = Assignment_SubmissionSerializer

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

class Assignment_PartnerViewSet(viewsets.ModelViewSet):
    queryset = Assignment_Partners.objects.all()
    serializer_class = Assignment_PartnerSerializer

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

class Assignment_GradingViewSet(viewsets.ModelViewSet):
    queryset = Assignment_Grading.objects.all()
    serializer_class = Assignment_GradingSerializer

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollement.objects.all()
    serializer_class = EnrollmentSerializer

    def destroy(self, request, *args, **kwargs):
    #  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        pass


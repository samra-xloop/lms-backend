from django.urls import path, include
from course.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'course',CourseViewSet)
router.register(r'module',ModuleViewSet)
router.register(r'units', UnitViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'files', FileViewSet)
router.register(r'quiz', QuizViewSet)
router.register(r'quiz_question', Quiz_QuestionViewSet)
router.register(r'question_option', Question_OptionViewSet)
router.register(r'quiz_submission', Quiz_SubmissionViewSet)
router.register(r'assignment', AssignmentViewSet)
router.register(r'assignment_submission', Assignment_SubmissionViewSet)
urlpatterns = [
    path('', include(router.urls))
]
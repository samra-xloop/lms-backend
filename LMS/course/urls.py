from django.urls import path, include
from course.views import *
from rest_framework.routers import DefaultRouter
# from rest_framework_nested.routers import NestedDefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'courses',CourseViewSet)
router.register(r'modules',ModuleViewSet)
router.register(r'units', UnitViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'files', FileViewSet)
# router.register(r'quiz', QuizViewSet)
# router.register(r'quiz_question', Quiz_QuestionViewSet)
# router.register(r'question_option', Question_OptionViewSet)
# router.register(r'quiz_submission', Quiz_SubmissionViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'assignment_submissions', Assignment_SubmissionViewSet)
router.register(r'assignment_partners', Assignment_PartnersViewSet)
# router.register(r'assignment_partners_group', Assignment_Partners_GroupViewSet)
router.register(r'assignment_gradings', Assignment_GradingViewSet)
router.register(r'enrollments', EnrollmentViewSet)
# router.register(r'assignment-submissions', AssignmentSubmissionViewSet)
# router.register(r'assignment_status', Assignment_StatusView)
# router.register(r'assignment_status', AssignmentStatusViewSet)
router.register(r'assignment_status', FilterViewSet)
#Filtration APIs 
# http://127.0.0.1:8000/api/assignment_status/filter_related_objects/?status=none
# http://127.0.0.1:8000/api/assignment_status/filter_related_objects/?status=pending
# http://127.0.0.1:8000/api/assignment_status/filter_related_objects/?status=pass
# http://127.0.0.1:8000/api/assignment_status/filter_related_objects/?status=fail


urlpatterns = [
    path('', include(router.urls)),
    path('categories/<int:category_id>/courses/', CourseByCategoryListView.as_view(), name='categories-courses-list'),
    path('courses/<int:course_id>/modules/', ModuleByCourseListView.as_view(), name='modules-courses-list'),
    path('modules/<int:module_id>/units/', UnitByModuleListView.as_view(), name='units-modules-list'),
    path('units/<int:unit_id>/videos/', VideoByUnitListView.as_view(), name='videos-units-list'),
    path('units/<int:unit_id>/files/', FileByUnitListView.as_view(), name='files-units-list'),
    path('units/<int:unit_id>/assignments/', AssignmentByUnitListView.as_view(), name='assignments-unitss-list'),
    path('assignments/<int:assignment_id>/assignment_submissions/', Assignment_SubmissionByAssignmentListView.as_view(), name='assignment_submissions-assignments-list'),
    path('assignments/<int:assignment_id>/assignment_partners/', Assignment_PartnersByAssignmentListView.as_view(), name='assignment_partners_group-assignments-list'),
    # path('assignment_partners_group/<int:assignment_group_id>/assignment_partners/', Assignment_PartnersByAssignment_Partners_GroupListView.as_view(), name='assignment_partners-assignment_partners_group-list'),
    path('assignment_submissions/<int:assignment_submission_id>/assignment_gradings/', Assignment_GradingByAssignment_SubmissionListView.as_view(), name='assignment_gradings-assingment_submissions-list'),
    path('courses/<int:course_id>/enrollments/', EnrollmentByCourseListView.as_view(), name='enrollments-courses-list'),
    path('categories/<int:category_id>/sub_categories/', SubCategoryListView.as_view(), name='sub_categories-categories-list'),
]
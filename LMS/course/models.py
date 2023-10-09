from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
# from accounts.models import CustomUser
from django.conf import settings
class Category(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='category_user')
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # slug = models.SlugField()
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE ,default=None, null=True, blank=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='category_updated_by')

    def __str__(self):
        return self.title     

class Course(models.Model):

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    # many courses can have same category.
    category = models.ManyToManyField(Category)      
    # slug = models.SlugField()
    created_at = models.DateField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_courses')   
    is_active = models.BooleanField(default=False)
    # updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateField(auto_now=True)
    course_image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='course_author')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='course_updated_by')
    
    def __str__(self):
        return self.title

class Module(models.Model):

    title = models.CharField(max_length=100)
    # one course can have multiple modules
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  
    # slug = models.SlugField()
    # description = models.TextField()
    created_at = models.DateField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateField(auto_now=True) 
    # updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='module_updated_by')

    class Meta:
        unique_together = ('course', 'title')

    def __str__(self):
        return self.title

class Unit(models.Model):

    # modules = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    # slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateField(auto_now=True)
    # updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='unit_updated_by')

    class Meta:
        unique_together = ('module', 'title')

    def __str__(self):
        return self.title

class Video(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateField(auto_now=True)
    # updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='video_updated_by')

    class Meta:
        unique_together = ('unit', 'title')


    def __str__(self):
        return self.title

class File(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True , blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    file = models.FileField(upload_to='Files/', blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateField(auto_now=True)
    # updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='files_updated_by')

    class Meta:
        unique_together = ('unit', 'title')


    def __str__(self):
        return self.title

# class Quiz(models.Model):
#     course = models.ForeignKey(Courses, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     # slug = models.SlugField()
#     description = models.TextField()
#     created_at = models.DateTimeField(default=timezone.now, editable=False)
#     updated_at = models.DateTimeField(auto_now=True)
#     # start_time = models.DateTimeField(default=timezone.now)
#     # end_time = models.DateTimeField(default=None)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     is_delete = models.BooleanField(default=False)
#     duration = models.TimeField(default=None)

# class Quiz_Question(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     question_text = models.TextField()
#     question_image = models.ImageField(upload_to='images/', null=True, blank=True)
# #need clarity here
#     question_type = models.CharField(max_length=50, default=None)

# class Question_Option(models.Model):
#     question = models.ForeignKey(Quiz_Question, on_delete=models.CASCADE)
#     option_text = models.TextField()
#     is_correct_option = models.BooleanField(default=False)

# # need clarity for this model.
# class Quiz_Submission(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, default=None)
#     # user = models.ForeignKey(user, on_delete=models.CASCADE)
#     started_at = models.DateTimeField(default=timezone.now)
#     time_taken_to_complete = models.DateTimeField(default=timezone.now)
#     score = models.CharField(max_length=100, default=None)


# #get it confirmed
class Assignment(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    due_date = models.DateField()
    due_time = models.TimeField()
    created_at = models.DateField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_team_submission_allowed = models.BooleanField(null=True, blank=True)
    Number_of_members = models.IntegerField(null=True, blank=True)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateField(auto_now=True)
    # updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    marks = models.CharField(max_length=10)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignment_updated_by')

    class Meta:
        unique_together = ('unit', 'title')

    def __str__(self):
        return self.title
    

class Assignment_Submission(models.Model):

    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignment_submission_done_by')
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now=True)
    content = models.FileField(upload_to='content/', null=True, blank=True)
    submitted_link = models.URLField()

# class Assignment_Partners_Group(models.Model):

#     assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
#     submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignment_submitted_by')

# class Assignment_Partners(models.Model):

#     # partners = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='partner')
#     partners = models.ManyToManyField(settings.AUTH_USER_MODEL)
#     assignment_group = models.ForeignKey(Assignment_Partners_Group, on_delete=models.CASCADE,related_name='assignment_group_number')
#     # submitted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Assignment_Grading(models.Model):

    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignment_doer')
    marks = models.CharField(max_length=3, null=True, blank=True)
    grading_datetime = models.DateTimeField(default=timezone.now)
    comments = models.TextField(null=True, blank=True)
    assignment_status = (('pass','PASS'),
                         ('fail','FAIL'),
                         ('pending','PENDING'))

    status = models.CharField(max_length=50, choices=assignment_status, default=assignment_status[2][0])
    assignment_submission = models.ForeignKey(Assignment_Submission, on_delete=models.CASCADE)
    # grader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    grader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignment_grader', null=True, blank=True)

class Enrollment(models.Model):

    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrolled_user')
    course = models.ManyToManyField(Course)
    enrollment_start_date = models.DateTimeField()
    enrollment_end_date = models.DateTimeField()
    is_active = models.BooleanField(default=False) 

# class Assignment_Status(models.Model):
#     submissions = models.ForeignKey(Assignment_Grading, on_delete=models.CASCADE, related_name='submissions_of_assignments')
    
 


#  QUIZ RETAKE model needs to be included. 






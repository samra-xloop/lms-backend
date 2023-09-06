from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# class Category(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

#     TRACK_1 = 'DEG'
#     TRACK_2 = 'CND'
#     TRACKS = (
#         (TRACK_1, 'Deg'),
#         (TRACK_2, 'Cnd')
#     )
#     name = models.CharField(max_length=100, choices=TRACKS, default=TRACK_1)
#     slug = models.SlugField()
#     short_description = models.TextField()
#     created_at = models.DateTimeField(auto_now=True)


#     def __str__(self):
#         return self.name

# class Module(models.Model):
#     categories = models.ManyToManyField(Category)  
#     name = models.CharField(max_length=100)
#     slug = models.SlugField()
#     short_description = models.TextField()
#     created_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name



# class Lecture(models.Model):
#     modules = models.ManyToManyField(Module)
#     name = models.CharField(max_length=100)
#     slug = models.SlugField()
#     short_description = models.TextField()
#     long_description = models.TextField()
#     video = models.FileField(upload_to='videos/', blank=True, null=True)
#     ppt_file = models.FileField(upload_to='ppt_files/', blank=True, null=True)
#     pdf_file = models.FileField(upload_to='pdf_files/', blank=True, null=True)
#     zip_file = models.FileField(upload_to='zip_file/', blank=True, null=True)
#     docs_file = models.FileField(upload_to='docs_file/', blank=True, null=True)
#     excel_file = models.FileField(upload_to='excel_file/', blank=True, null=True)
#     image = models.ImageField(upload_to='image_file/', blank=True, null=True)
#     ACTIVE = 'active'
#     NON_ACTIVE = 'non-active'
#     ASSIGNMENT = 'assignment'
#     QUIZ = 'quiz'
#     LECTURE = 'lecture'
#     ANNOUNCEMENT = 'announcement'
    
#     STATUS_OPTIONS = (
#         (ACTIVE,'Active'),
#         (NON_ACTIVE,'Non-Active')
#     )

#     LESSON_TYPE = (
#         (ASSIGNMENT,'Assignment'),
#         (QUIZ,'Quiz'),
#         (LECTURE,'Lecture'),
#         (ANNOUNCEMENT, 'Announcement')
#     )

#     status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default=ACTIVE)
#     lesson_type = models.CharField(max_length=20, choices=LESSON_TYPE, default=LECTURE)

#     def __str__(self):
#         return self.name

class Category(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # TRACK_1 = 'DEG'
    # TRACK_2 = 'CND'
    # TRACKS = (
    #     (TRACK_1, 'Deg'),
    #     (TRACK_2, 'Cnd')
    # )
    # slug = models.SlugField()
    # created_at = models.DateTimeField(default=timezone.now, editable=False)
    # updated_at = models.DateTimeField(auto_now=True)

    # title = models.CharField(max_length=100, choices=TRACKS, default=TRACK_1)
    title = models.CharField(max_length=100, default=None)
    description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE ,default=None, null=True, blank=True)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title     

class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # many courses can have same category.
    category = models.ManyToManyField(Category, default=None, null=True, blank=True)      
    # slug = models.SlugField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(user, on_delete=models.CASCADE)   
    is_active = models.BooleanField(default=False)
    # updated_by = models.ForeignKey(user, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Module(models.Model):
    title = models.CharField(max_length=100)
    # one course can have multiple modules
    course = models.ForeignKey(Courses, default=None, on_delete=models.CASCADE)  
    # slug = models.SlugField()
    # description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=timezone.now)
    # updated_by = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Units(models.Model):
    # modules = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    module = models.ForeignKey(Module, default=None, on_delete=models.CASCADE)
    # slug = models.SlugField()
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=None)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=timezone.now)
    # updated_by = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Videos(models.Model):
    title = models.CharField(max_length=100, default=None)
    description = models.TextField(default=None)
    url = models.URLField(blank=True, null=True)
    unit = models.ForeignKey(Units, default=None, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=timezone.now)
    # updated_by = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Files(models.Model):
    title = models.CharField(max_length=100, default=None)
    description = models.TextField(default=None)
    url = models.URLField(blank=True, null=True)
    unit = models.ForeignKey(Units, default=None, on_delete=models.CASCADE)
    file = models.FileField(upload_to='Files/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=timezone.now)
    # updated_by = models.ForeignKey(user, on_delete=models.CASCADE)

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
    description = models.TextField
    unit = models.ForeignKey(Units, on_delete=models.CASCADE, default=None)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now, editable= False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_team_submission_allowed = models.BooleanField(default=False)
    Number_of_members = models.IntegerField(default=1)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=timezone.now)
    # updated_by = models.ForeignKey(user, on_delete=models.CASCADE)
    marks = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.title

class Assignment_Submission(models.Model):
    # user_id = models.ForeignKey(user_id, on_delete=models.CASCADE)
    # assignment_id = models.ForeignKey(assignment_id, on_delete=models.CASCADE)
    # submitted_by = models.ForeignKey(user, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE, default=None)
    submiission_date = models.DateTimeField(default=timezone.now, editable=False)
    content = models.FileField(upload_to='content/', default=None)

class Assignment_Partners(models.Model):
    # name = models.ForeignKey(user, on_delete=models.CASCADE)
    # partners = models.ForeignKey(user, on_delete=models.CASCADE, default=None)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    # submitted_by = models.ForeignKey(user, on_delete=models.CASCADE)

class Assignment_Grading(models.Model):
    # user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    marks = models.CharField(max_length=3, default=None)
    grading_datetime = models.DateTimeField(default=timezone.now, editable=False)
    comments = models.TextField()

    assignment_status = (('pass','PASS'),
                         ('fail','FAIL'),
                         ('pending','PENDING'))

    status = models.CharField(max_length=50, choices=assignment_status)
    submission = models.ForeignKey(Assignment_Submission, on_delete=models.CASCADE)
    # grader_id = models.ForeignKey(user, on_delete=models.CASCADE)

class Enrollement(models.Model):
    # user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    course = models.ManyToManyField(Courses, default=None)
    enrollment_start_date = models.DateTimeField(default=timezone.now)
    enrollment_end_date = models.DateTimeField()
    is_active = models.BooleanField(default=False) 

#QUIZ RETAKE model needs to be included. 







from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models import Q



class Author(models.Model):

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creator')
    editor = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True)

class Category(models.Model):

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='category_created_by')
    created_at = models.DateField(auto_now=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE ,default=None, null=True, blank=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='category_updated_by')

    def __str__(self):
        return self.title     

class Course(models.Model):

    instructor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='course_creator')
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(Category)      
    created_at = models.DateField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateField(auto_now=True)
    course_image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='course_updated_by')

    def __str__(self):
        return self.title



class Module(models.Model):

    instructor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='module_creator')
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  
    created_at = models.DateField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateField(auto_now=True) 
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='module_updated_by')

    class Meta:
        unique_together = ('course', 'title')

    def __str__(self):
        return self.title



class Unit(models.Model):

    instructor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='unit_creator')
    title = models.CharField(max_length=100)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='unit_updated_by')

    class Meta:
        unique_together = ('module', 'title')

    def __str__(self):
        return self.title



class Video(models.Model):

    instructor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='video_creator')
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
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='video_updated_by')
    completion = models.BooleanField(default=False)
    learner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE ,related_name='video_learner')


    class Meta:
        unique_together = ('unit', 'title')


    def __str__(self):
        return self.title

class File(models.Model):

    instructor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='file_creator')
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
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='files_updated_by')
    completion = models.BooleanField(default=False)
    learner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE ,related_name='file_learner')


    class Meta:
        unique_together = ('unit', 'title')

class Resource(models.Model):

    instructor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='resource_creator')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True , blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    resource = models.FileField(upload_to='Resources/', blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resources_updated_by')

    class Meta:
        unique_together = ('unit', 'title')        


    def __str__(self):
        return self.title


class Assignment(models.Model):

    instructor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='assignment_creator')
    title = models.CharField(max_length=100)
    description = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    due_date = models.DateField()
    due_time = models.TimeField()
    created_at = models.DateField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_team_submission_allowed = models.BooleanField(default=False)
    Number_of_members = models.IntegerField(null=True, blank=True)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateField(auto_now=True)
    marks = models.CharField(max_length=10)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignment_updated_by')
    assignment_file = models.FileField(upload_to='assignment_file', null=True, blank=True)
    completion = models.BooleanField(default=False)
    learner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE ,related_name='assignment_learner')

    class Meta:
        unique_together = ('unit', 'title')

    def __str__(self):
        return self.title
    
        
class Assignment_Partners_Group(models.Model):

    instructor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='assignment_partners_group_creator')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    
class Assignment_Partners(models.Model):

    partners = models.ManyToManyField(settings.AUTH_USER_MODEL)
    assignment_group = models.ForeignKey(Assignment_Partners_Group, on_delete=models.CASCADE,related_name='assignment_number')
    instructor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='assignment_partners_creator')

class Assignment_Submission(models.Model):

    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignment_submission_done_by')
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now=True)
    content = models.FileField(upload_to='content/', null=True, blank=True)
    submitted_link = models.URLField()
    submission_time = models.TimeField(auto_now=True)


class Assignment_Grading(models.Model):

    marks = models.CharField(max_length=3, null=True ,blank=True)
    is_graded = models.BooleanField(default = False)
    grading_datetime = models.DateTimeField(auto_now=True)
    comments = models.TextField(null=True, blank=True)
    assignment_status = (('Pass','PASS'),
                         ('Not Passed','FAIL'),
                         ('Pending','PENDING'))

    status = models.CharField(max_length=50, choices=assignment_status, default=assignment_status[2][0])
    assignment_submission = models.ForeignKey(Assignment_Submission, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='assignment_grading_creator', null=True, blank=True)


class Enrollment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrolled_user')
    course = models.ManyToManyField(Course)
    enrollment_start_date = models.DateTimeField()
    enrollment_end_date = models.DateTimeField()
    is_active = models.BooleanField(default=False) 
   
 



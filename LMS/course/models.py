from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
   
    TRACK_1 = 'DEG'
    TRACK_2 = 'CND'
    TRACKS = (
        (TRACK_1, 'Deg'),
        (TRACK_2, 'Cnd')
    )
    name = models.CharField(max_length=100, choices=TRACKS, default=TRACK_1)
    description = models.TextField()
    
    def __str__(self):
        return self.name    


class Courses(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    



    def __str__(self):
        return self.name

class Module(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, default=None)  
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=None)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Units(models.Model):
    modules = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=None)
    is_delete = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name

class Videos(models.Model):
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/', blank=True, null=True)

class Files(models.Model):
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    file = models.FileField(upload_to='Files/', blank=True, null=True)

class Quiz(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    start_time = models.TimeField()
    end_time = models.TimeField()

class Quiz_Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()

class Question_Option(models.Model):
    question = models.ForeignKey(Quiz_Question, on_delete=models.CASCADE)
    option_text = models.TextField()
    is_correct_option = models.BooleanField(default=False)

# need clarity for this model.
class Quiz_Submission(models.Model):
    row_1 = models.TextField()
    row_2 = models.TextField()
    row_3 = models.TextField()        

#get it confirmed
class Assignment(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now, editable= False)
    updated_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Assignment_Submission(models.Model):
    submiission_date = models.DateTimeField()



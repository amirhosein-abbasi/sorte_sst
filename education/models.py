from tabnanny import verbose
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


auth_user = settings.AUTH_USER_MODEL if getattr(
    settings, "AUTH_USER_MODEL") else User


class Quiz(models.Model):
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE, null=True, blank=True)
    question = models.CharField(max_length=200)
    answer1 = models.CharField(max_length=400)
    answer2 = models.CharField(max_length=400)
    answer3 = models.CharField(max_length=400)
    answer4 = models.CharField(max_length=400)
    correct_answer = models.CharField(max_length=400)
    chapter = models.IntegerField(default=1)
    passed = models.BooleanField(default=False)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'Quizes'
        verbose_name_plural = 'Quizes'



CHOICES = (
  ('DONE', 'DONE'),
  ('None', 'None'),
)
STATUS = (
    ('Open', 'Open'),
    ('Locked', 'Locked')
)


class CourseModel(models.Model):
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE, null=True, blank=True)
    chapter = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    # lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='None')

    def __str__(self):
        return self.title
    

LESSON_STATUS = (
    ('Done', 'Done'),
    ('Pending', 'Pending')
)

class LessonModel(models.Model):
    chapter = models.IntegerField(default=1)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d/', null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,null=True,blank=True)
    number = models.IntegerField(default=1)
    point = models.FloatField(default=3.39)
    status = models.CharField(max_length=20, choices=LESSON_STATUS, default='Pending' )

    def __str__(self):
        return self.title

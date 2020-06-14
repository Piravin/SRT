from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User,default=1, on_delete=models.SET_DEFAULT)
    overview = models.TextField(blank=True)

    class __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=100)
    parent_course = models.ForeignKey(Course, on_delete=models.CASCADE)

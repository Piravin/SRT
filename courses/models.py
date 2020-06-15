from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User,default=1, on_delete=models.SET_DEFAULT)
    overview = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=100)
    parent_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.author

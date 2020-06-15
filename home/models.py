from django.db import models

class Item(models.Model):
    logo = models.ImageField(default='logo.png',upload_to='logo',blank=True)
    quote1 = models.CharField(default="SASTRA Racing Team", max_length=20) 
    quote2 = models.CharField(default="SASTRA Racing Team", max_length=20,blank=True)
    backgroundimage1 = models.ImageField(default='back1.jpg',upload_to='back1',blank=True)
    backgroundimage2 = models.ImageField(default='back2.jpg',upload_to='back2',blank=True)
    video = models.CharField(max_length=1000,blank=True)
    video_description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    contacts = models.TextField(blank=True)


class Slide(models.Model):
    title = models.CharField(max_length=100)
    slide_link = models.CharField(max_length=1000,default='#', blank=True)
    slide = models.ImageField(upload_to='slides')

    def __str__(self):
        return self.title

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    sponsor = models.ImageField(upload_to="sponsors")
    sponsor_link = models.CharField(max_length=1000,blank=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField(blank=True)
    subject = models.TextField(blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name
    

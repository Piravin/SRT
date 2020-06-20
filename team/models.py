from django.db import models

class Team(models.Model):
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.year


class Car(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.team.year

class TeamMember(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField(default="default.png",upload_to="Team_profile_pics")
    role = models.CharField(max_length=100,default="member",blank=True)
    year_of_study = models.CharField(max_length=1)
    subsystem = models.CharField(max_length=100)
    linked_in = models.CharField(max_length=1000,default="#")
    description = models.TextField()

    def __str__(self):
        return self.name

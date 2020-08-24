from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    # create one to one relationship to Django User class
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
    )

    #additional classes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class Team(models.Model):
    position = models.IntegerField()
    team_name = models.CharField(max_length=30)
    points = models.IntegerField()

    def __str__(self):
        return 'Team : {0}'.format(self.team_name)

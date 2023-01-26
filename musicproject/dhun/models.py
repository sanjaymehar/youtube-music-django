from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse
from django.core.validators import FileExtensionValidator,RegexValidator

class Album(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    release=models.DateField(default=now)
    genre=models.CharField(max_length=100)
    image=models.FileField(validators=[FileExtensionValidator(['jpg','png','gif'])])

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('dhun:home')




class Song(models.Model):
    alid=models.ForeignKey(Album,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    lyricists=models.CharField(max_length=100)
    file=models.FileField(validators=[FileExtensionValidator(['mp3','aac','wav','mp4'])])

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('dhun:song',kwargs={'pk':self.id})

class Profile(models.Model):
    uid=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10,validators=[RegexValidator('^[9,7,8,6]\d{9}$','invalid phone number')])
    photo=models.FileField(validators=[FileExtensionValidator(['jpg','png','gif'])])
    bio=models.TextField(max_length=1000)

    def __str__(self):
        return self.uid.username + ','+self.phone
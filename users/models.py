from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.deletion import SET_NULL
# Create your models here.

from django.db.models.signals import post_save, post_delete

#class Person(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    #created = models.DateTimeField(auto_now_add=True)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    #def __str__(request):
     #   return request.name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=300, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    intro = models.CharField(max_length=500, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField('skill', blank=True )
    other_skill = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank =True, null= True, upload_to = 'profiles/', default = 'profiles/defaultP.jpeg')
    instagram_link = models.CharField(max_length=200, blank=True, null=True)
    facebook_link = models.CharField(max_length=200, blank=True, null=True)
    linkedin_link = models.CharField(max_length=200, blank=True, null=True)
    youtube_link = models.CharField(max_length=200, blank=True, null=True)
    website_link = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)
    


class Skill(models.Model):
    name = models.CharField(max_length=200, )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(request):
        return request.name


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True,  )
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages' )
    senderName = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=300, blank=False, null=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.senderName)

    class Meta:
        ordering = ['is_read', '-created']

    
    




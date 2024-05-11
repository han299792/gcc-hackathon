from django.db import models
from account.models import User
from django.utils import timezone
import base64


# Create your models here.

class place_tag(models.Model):
    name = models.CharField(max_length = 30)

class mood_status(models.Model): #본인 기분
    type = models.CharField(max_length=30)
    color = models.CharField(max_length=30)

class place(models.Model):
    place_name = models.CharField(max_length=30)
    explanation = models.CharField(max_length=10000)
    lat = models.FloatField()
    lng = models.FloatField()
    photo = models.ImageField(upload_to="", blank=True)
    PLACE_TAG={
        "1":"나무가 울창한",
        "2":"쾌적한 실내", 
        "3":"여러명",
        "4":"나홀로",
        "5":"조용한",
        "6":"인기",
    }
    place_tag = models.ForeignKey(place_tag, null = True, choices=PLACE_TAG)

class post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    place_id = models.ForeignKey(place, related_name='posts', on_delete=models.CASCADE)
    created_date =models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    mood_status = models.ForeignKey(mood_status, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100000)
    photo = models.ImageField(upload_to="", blank=True)

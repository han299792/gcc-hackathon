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

class mood_tag(models.Model): #장소에 관련된 주관적 감정
    name = models.CharField(max_length=30)

class place(models.Model):
    place_name = models.CharField(max_length=30)
    lat = models.FloatField()
    lng = models.FloatField()
    place_tag = models.ForeignKey(place_tag, null = True, on_delete=models.SET_NULL)
    mood_tag = models.ForeignKey(mood_tag, null = True, on_delete=models.SET_NULL)
    photo = models.ImageField(upload_to="", blank=True)

class post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    place_id = models.ForeignKey(place, on_delete=models.CASCADE)
    created_date =models.DateTimeField(timezone.now)
    updated_date = models.DateTimeField(null=True)
    mood_status = models.ForeignKey(mood_status, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100000)
    photo = models.ImageField(upload_to="", blank=True)
    mood_tag = models.ForeignKey(mood_tag, null=True, on_delete=models.SET_NULL)


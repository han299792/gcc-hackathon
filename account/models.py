from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, name, password=None):
        if not email:
            raise ValueError('email을 입력하세요')
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname, 
            name = name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create(self, email, nickname, name, password=None) -> Any:
        user = self.create_user(
            email,
            password = password,
            nickname = nickname,
            name = name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False)

    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'nickname'
    
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.nickname
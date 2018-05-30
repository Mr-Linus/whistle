from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
import hashlib
import random
# from django.utils.timezone import now
# Create your models here.


class ShadowUserManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('QQ', '')
        extra_fields.setdefault('sex', 'M')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, email, password, **extra_fields)

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('QQ', '')
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('sex', 'M')
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    GENDER_CHOICES = (
        ('F', '女'),
        ('M', '男'),
        ('U','未知')
    )
    email = models.EmailField(_('email address'), blank=True)
    QQ = models.CharField(default='', max_length=60)
    status = models.BooleanField(default=False, verbose_name="Status")
    sex = models.CharField(max_length=2, choices=GENDER_CHOICES, default='M')
    objects = ShadowUserManager()

    def get_avatar(self):
        return hashlib.md5(self.email.encode()).hexdigest()



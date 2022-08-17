from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from ads.models import Location


class User(AbstractBaseUser):
    ROLES = [
        ('admin', 'администратор'),
        ('member', 'пользователь'),
        ('moderator', 'модератор')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=ROLES, default='member')
    age = models.SmallIntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    dept_choices = (
        ('KYC', '科研管理处'),
        ('DZZ', '大装置部'),
    )
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,)

    cellphone = models.CharField(max_length=15)
    department = models.CharField(max_length=3,
                                  choices=dept_choices,
    )

    def __str__(self):
        return self.user.username
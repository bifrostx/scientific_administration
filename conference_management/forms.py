# -*- coding:utf-8 -*-
from django import forms
from .models import UserProfile


class UserProfileForm(forms.Form):
    last_name = forms.CharField(max_length=30, label="姓")
    first_name = forms.CharField(max_length=30, label="名")
    department = forms.CharField(max_length=3, label="所属部门")
    cellphone = forms.CharField(max_length=15, label="手机号码")

    class Meta:
        model = UserProfile
        fields = ('last_name', 'first_name', 'cellphone', 'department')
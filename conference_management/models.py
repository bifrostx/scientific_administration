# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
DEPT_CHOICES = (
        ('HWL', '核物理研究室'),
        ('WSW', '物理生物学研究室'),
        ('SKX', '水科学研究室'),
        ('JSQ', '加速器物理与射频技术部'),
        ('FEL', '自由电子激光技术部'),
        ('SLK', '束流测量与控制技术部'),
        ('JXG', '机械工程技术部'),
        ('DYJ', '电源技术部'),
        ('GYS', '公用设施技术部'),
        ('JAJ', '上海光源建安技术部'),
        ('SMK', '生命科学研究部'),
        ('WLH', '物理与环境科学研究部'),
        ('CLN', '材料与能源科学研究部'),
        ('XJC', '先进成像与工业应用研究部'),
        ('SXJ', '束线机械工程技术部'),
        ('SXG', '束线光学工程技术部'),
        ('YYJ', '应用加速器研究室'),
        ('FYD', '反应堆物理部'),
        ('RYJ', '熔盐机械工程技术部'),
        ('DXT', '反应堆系统工程技术部'),
        ('RYH', '熔盐化学与工程技术部'),
        ('DCL', '堆材料与工程技术一部'),
        ('FSH', '放射化学与工程技术部'),
        ('HAQ', '核安全与工程技术部'),
        ('DYG', '堆材料与工程技术二部'),
        ('HNJ', '核能建安工程技术部'),
        ('BGS', '办公室'),
        ('KYC', '科研管理处'),
        ('DKX', '大科学装置管理部'),
        ('HNG', '核能管理部'),
        ('RJC', '人事教育处'),
        ('CWC', '财务处'),
        ('TJC', '科研条件处'),
        ('KFC', '科技开发处'),
        ('YJS', '研究生部'),
        ('ZGC', '综合管理处'),
        ('JAB', '技术安全技术部'),
        ('XXZ', '信息中心'),
        ('ZCG', '经营性资产管理中心'),
        ('HQF', '后勤服务中心'),
        ('HXH', '核学会'),
        ('RHT', '日环投资公司'),
        ('SLG', '世龙科技公司'),
        ('FZZ', '辐照中心'),

    )
class UserProfile(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,)

    cellphone = models.CharField(max_length=15,
                                 verbose_name="手机号码",)
    department = models.CharField(max_length=3,
                                  verbose_name="所属部门",
                                  choices=DEPT_CHOICES,
    )

    def __str__(self):
        return self.user.username


class Conference(models.Model):
    name = models.CharField(max_length=100, verbose_name="会议名称")
    department = models.CharField(max_length=3,
                                  verbose_name="所属部门",
                                  choices=DEPT_CHOICES,
    )
    applicant = models.ForeignKey(User, verbose_name="申请人")
    reason = models.CharField(max_length=200, verbose_name="申请原因")
    chair = models.CharField(max_length=30, verbose_name="会议负责人")
    start_date = models.DateField(verbose_name="会议开始时间")
    end_date = models.DateField(verbose_name="会议结束时间")
    place = models.CharField(max_length=30, verbose_name="会议地点")
    scale = models.IntegerField()
    source = models.CharField(max_length=45, verbose_name="课题卡号")
    note = models.CharField(max_length=200, verbose_name="说明")

    def __str__(self):
        return self.name


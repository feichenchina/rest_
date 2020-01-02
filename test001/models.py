from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    role_choice = ((1, '管理员'), (2, '普通用户'))
    role = models.IntegerField(choices=role_choice)


class BWH(models.Model):
    '''三国信息'''
    bust = models.IntegerField(verbose_name='吕布')
    waist = models.IntegerField(verbose_name='刘邦')
    hips = models.IntegerField(verbose_name='韩信')

    user = models.OneToOneField(to=UserInfo,on_delete=models.CASCADE)
#!/usr/bin/python3
#可用的预定义文件模板变量为：
# 当前项目的名称-->yiguo
#文件名---》celery
#用户名---》Administrator
#日期-----》2019/10/29 
#时间-----》22:03
#功能-----》
from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_frame.settings')


app = Celery('rest_frame')     #这里改成自己工程名

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
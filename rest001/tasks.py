#!/usr/bin/python3
#可用的预定义文件模板变量为：
# 当前项目的名称-->yiguo
#文件名---》task
#用户名---》Administrator
#日期-----》2019/10/29
#时间-----》21:45
#功能-----》
import os

from celery import task
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings


@task
def send_email(email,code):
    print('这里是异步请求开始')
    title = "修改密码"
    msg = "您好，你的验证码为" + code['code']
    from_email = "3069582567@qq.com"
    print('email',email)
    recievers = [email, ]
    try:
        res = send_mail(title, msg, from_email, recievers,)
        print(res)
        print('2222222222')
    except Exception as e:
        print(e,'111111111')
    print('这里是结束')
    return "这里是结束"


@task
def add1(x, y):
    print('进入add1中')
    return x + y




# @task
# def send_register_email(email):
#
#     subject, from_email, to = "注册", os.environ.get('EMAIL_HOST_USER'), \
#                               email
#     text_content = "{{ user.username }}，你好\
#                     欢迎来到 Ulysses\
#                     为了验证您的账户，请点击以下链接进行验证\
#                     链接\
#                     Ulysses\
#                     请勿回复此邮件"
#     # html_content = f"<p>{user.username}， 你好</p>\
#     #                 <p>欢迎来到 <b>Ulysses</b>!</p>\
#     #                 <p>为了验证您的账户，请点击进行验证</p>\
#     #                 <p>或者您可以在浏览器被输入以下内容：</p>\
#     #                 <p>链接</p>\
#     #                 <p>Ulysses</p>\
#     #                 <p><small>请勿回复此邮件</small></p>"
#     email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=from_email, to=[to])
#     # email.attach_alternative(html_content, 'text/html')
#     # email.attach_alternative()
#     # 添加附件
#     # email.attach_file('users/templates/email/confirm.html', 'text/plain')
#     # email.attach_file('users/templates/email/confirm.txt', 'text/html')
#     email.send()


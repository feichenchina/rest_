from rest_framework.permissions import BasePermission
from test001 import models


class AdminPermission(BasePermission):
    '''管理员权限认证'''
    message = '您没有权限访问！'

    def has_permission(self, request, view):
        user_id = request.GET.get('uid')
        user = models.UserInfo.objects.filter(pk=user_id).first()

        if not user or user.role == 2:
            return True
        else:
            return True
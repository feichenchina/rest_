from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from test001 import models


class BlackNameAuth(BaseAuthentication):
    '''黑名单认证'''

    def authenticate(self, request):
        BLACK_NAME_LIST = ['小花', '小翠']

        # 通过从url获取user_id的方式模拟用户登录
        user_id = request.GET.get('uid')
        user = models.UserInfo.objects.filter(pk=user_id).first()

        if not user or user.username in BLACK_NAME_LIST:
            raise AuthenticationFailed('您没有登录或者被关小黑屋啦')
        else:
            return user.username, user_id
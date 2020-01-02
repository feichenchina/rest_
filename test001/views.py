from django.contrib.auth.models import User
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, HTMLFormRenderer, AdminRenderer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import action

from test001.serializers import BWHModelSerializer,UserModelSerializer
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.viewsets import ModelViewSet
from test001 import models
from test001.auth import BlackNameAuth
from test001.permission import AdminPermission
from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    '''分页，自定义每页显示2条'''
    page_size = 2


class BWHViewSet(ModelViewSet):
    '''在黑名单中的用户禁止查看三国信息'''
    authentication_classes = [BlackNameAuth]
    # 分页
    pagination_class = MyPagination
    serializer_class = BWHModelSerializer
    queryset = models.BWH.objects.all()


class UserViewSet(ModelViewSet):
    '''非管理员禁止查看用户信息'''
    permission_classes = [AdminPermission]
    # 分页
    pagination_class = MyPagination
    serializer_class = UserModelSerializer
    queryset = models.UserInfo.objects.all()

    renderer_classes = [JSONRenderer,HTMLFormRenderer,AdminRenderer]

    def list(self, request):
        queryset = models.UserInfo.objects.all()
        response = {
            'code': 0,
            'data': [],
            'msg': 'success',
            'total': ''
        }
        serializer = self.get_serializer(queryset, many=True)
        if serializer:
            response['data'] = serializer.data
            response['total'] = len(serializer.data)
            return Response(response)
        else:
            response['code'] = 1
            response['msg'] = 'error'
            response['total'] = 0
            return Response(response,status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        response = {
            'code': 0,
            'data': [],
            'msg': 'success',
        }
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        if serializer:
            response['data'] = serializer.data
            return Response(response)
        else:
            response['code'] = 1
            response['msg'] = 'error'
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # return JsonResponse(data=serializer.data, code=200, msg="success", status=status.HTTP_200_OK)

    def get_queryset(self,pk=None):
        if pk:
            return models.UserInfo.objects.filter(id=pk)
        else:
            return models.UserInfo.objects.all()

    @action(methods=['post'], detail=True,
            url_path='change-password', url_name='change_password')
    def set_password(self, request, pk=None):
        user_pk = self.get_queryset(pk)
        if user_pk:
            user = models.UserInfo.objects.filter(id=pk).first()
            # partial 字段用来设置允许局部更新，否则所有必填字段都必须填入，否则会报错
            ser_obj = self.get_serializer(instance=user, data=request.data, partial=True)
            if ser_obj.is_valid():
                ser_obj.save()
                return Response(ser_obj.validated_data)
            else:
                return Response(ser_obj.errors)
        else:
            return Response(data={"msg":"id is not found"},status=status.HTTP_404_NOT_FOUND)


    # 用来创建一个新用户
    @action(methods=['post'], detail=True,
            url_path='create_user', url_name='create_user')
    def create_user(self, request, pk=None):
        data = request.data
        if data:
            ser_obj = self.get_serializer(data = request.data)
            if ser_obj.is_valid():
                print(ser_obj)
                print(ser_obj.validated_data)
                ser_obj.save()
                return Response(ser_obj.validated_data)
            else:
                return Response(ser_obj.errors)
        else:
            return Response(data={"msg": "not find message"}, status=status.HTTP_404_NOT_FOUND)


class Test2ViewSet(View):
    def get(self,request):
        return HttpResponse('123')



def api_s(request):

    pass



class UserDetail(generics.RetrieveAPIView):
    """
    A view that returns a templated HTML representation of a given user.
    """
    queryset = User.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    #
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'user': self.object}, template_name='user_detail.html')



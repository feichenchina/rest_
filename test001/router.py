from rest_framework import routers

from test001 import views

routers = routers.DefaultRouter()
# router.register('test', Test1ViewSet, base_name='test')
# test_router = routers.NestedSimpleRouter(router, r'test', lookup='test1')
# router.register(r'test', test, basename='test')
routers.register('bwh',views.BWHViewSet)
routers.register('user',views.UserViewSet)
# routers.register('UserDetail',views.UserDetail)
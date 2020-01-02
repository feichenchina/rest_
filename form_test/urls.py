from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'get_name/',views.get_name,name='get_name'),
    url(r'test_002/',views.test_002,name='test_002'),
]

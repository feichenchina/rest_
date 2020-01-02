from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from test001 import views

urlpatterns = [
    url(r'Test2ViewSet',views.Test2ViewSet.as_view())
]
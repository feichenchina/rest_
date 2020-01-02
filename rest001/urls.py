from django.conf.urls import url
from rest001 import views

urlpatterns = [
    url(r'login',views.login,name='login'),
    url(r'register',views.register,name='register'),
    url(r'download',views.download,name='download'),
    # url(r'first_celery',views.first_celery,name='first_celery'),
    # url(r'serch_result',views.serch_result,name='serch_result'),
    url(r'show_pdf',views.show_pdf,name='show_pdf'),
    url(r'run_pdf',views.run_pdf,name='run_pdf'),
    url(r'get_info',views.get_info,name='get_info'),
]
from django.db import models

# Create your models here.
class User_info(models.Model):
    email = models.CharField(max_length=22,verbose_name='email')
    password = models.CharField(max_length=20,verbose_name='password')

    class Meta:
        db_table = 'user_info'

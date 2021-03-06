# Generated by Django 3.0 on 2019-12-23 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('role', models.IntegerField(choices=[(1, '管理员'), (2, '普通用户')])),
            ],
        ),
        migrations.CreateModel(
            name='BWH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bust', models.IntegerField(verbose_name='吕布')),
                ('waist', models.IntegerField(verbose_name='刘邦')),
                ('hips', models.IntegerField(verbose_name='韩信')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='test001.UserInfo')),
            ],
        ),
    ]

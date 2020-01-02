from rest_framework import serializers
from test001 import models


class BWHModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BWH
        fields = '__all__'


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = '__all__'

    # 对全局数据进行校验
    def validate(self, data):
        """
        Check that start is before finish.
        """
        print(data)
        try:
            if data['start'] > data['finish']:
                raise serializers.ValidationError("finish must occur after start")
            return data
        except Exception as e:
            pass
            # data = 'start or finish is not found'
        # raise serializers.ValidationError('start or finish is not found')
        return data
    # 对密码进行校验
    def validate_password(self, value):
        """
        Check that the blog post is about Django.
        """
        if '1' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value

    def update(self, instance, validated_data):
        # profile_data = validated_data.pop('profile')
        # Unless the application properly enforces that this field is
        # always set, the follow could raise a `DoesNotExist`, which
        # would need to be handled.
        # profile = instance.profile

        instance.password = validated_data.get('password', instance.password)
        # instance.email = validated_data.get('email', instance.email)
        instance.save()
        # profile.is_premium_member = profile_data.get(
        #     'is_premium_member',
        #     profile.is_premium_member
        # )
        # profile.has_support_contract = profile_data.get(
        #     'has_support_contract',
        #     profile.has_support_contract
        # )
        # profile.save()

        return instance

    def create(self, validated_data):
        return models.UserInfo.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role'],
            # email=validated_data['email'],
            # is_premium_member = validated_data['profile']['is_premium_member'],
            # has_support_contract = validated_data['profile']['has_support_contract']
            )
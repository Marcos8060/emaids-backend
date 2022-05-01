from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50,min_length=6,write_only=True)
    # profiles = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())
    class Meta:
        model = User
        fields = ['email','username','password']
    
    def create(self,validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    # user = RegisterUserSerializer()
    # pub_date=serializers.DateField(format=None,input_formats=None)
    class Meta:
        model = Comment
        fields = ['id','profile','comment','user']


class ProfileSerializer(serializers.ModelSerializer):
    profile_comment = CommentSerializer(read_only=True,many=True)
    # owner = serializers.ReadOnlyField(source='owner.user_name')
    class Meta:
        model = Profile
        fields = ['id','image','full_name','email','age','location','experience','contract','bio','profile_comment']
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    options=(('user','user'),('coach','coach'),)
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    role=serializers.ChoiceField(choices=options)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','password2','role']
        extra_kwargs = {'password': {'write_only': True}}
    def save(self):
        password1=self.validated_data['password']
        password2=self.validated_data['password2']
        if password1 !=password2:
            raise serializers.ValidationError({'error':'passwords do not match'})


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']
        extra_kwargs = {'email':{'required':True},'password': {'write_only': True}}


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'
    
        
        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
        extra_kwargs={'profile':{'required':False}}


class ChangePasswordSerializer(serializers.ModelSerializer):
    
    old_password=serializers.CharField(style={'input_type':'password'}, write_only=True)
    new_password=serializers.CharField(style={'input_type':'password'}, write_only=True)
    confirm_password=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model=User
        fields=['old_password','new_password','confirm_password']
        extra_kwargs = {
                        'old_password': {'write_only': True},
                        'new_password': {'write_only': True},
                        'confirm_password': {'write_only': True}
                        }


class RequestPasswordResetEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email']
        extra_kwargs = {'email':{'required':True}}

from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

class CustomUserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField()
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture']

    #User creation serializer
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'], 
            bio=validated_data['bio'], 
            profile_picture=validated_data['profile_picture'], **validated_data)
        
        #Token creation for the new user
        Token.objects.create(user=user)
        return user
      

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        token, created = Token.objects.get_or_create(user=user)
        return {'token': token.key, 'user': user.username}
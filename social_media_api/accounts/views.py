from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from accounts.models import CustomUser
from rest_framework import authentication

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        user = CustomUser.objects.create_user(username=username, password=password, email=email)
        token, created = Token.objects.get_or_create(user=user)

        if (user and token):
            return Response({'token': token.key, 'user': UserSerializer(user).data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'Something happend'}, status=status.HTTP_400_BAD_REQUEST)
    
        

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': UserSerializer(user).data}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def get(self, request):
        #Returns the profile details of the authenticated user.
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.follow(user_to_follow)
        return Response({"message": "User followed successfully"}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.unfollow(user_to_unfollow)
        return Response({"message": "User unfollowed successfully"}, status=status.HTTP_200_OK)

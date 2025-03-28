from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
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

    def get(self, request):
        #Returns the profile details of the authenticated user.
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
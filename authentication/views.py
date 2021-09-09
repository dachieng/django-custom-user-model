from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from authentication.serializers import LoginSerializer, UserSerializer
from authentication.models import User
from django.contrib.auth import authenticate
from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView
import jwt
from django.conf import settings


class APIAuthUser(GenericAPIView):
    # access the api endpoint with token authentication
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response({'user': serializer.data})


class UserVieset(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(CreateAPIView):
    authentication_classes = []

    serializer_class = LoginSerializer

    def create(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')
        user = authenticate(username=email, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.SECRET_KEY, algorithm="HS256")

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}
            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

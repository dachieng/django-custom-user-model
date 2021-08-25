from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from authentication.serializers import LoginSerializer, UserSerializer
from rest_framework.views import APIView
from authentication.models import User
from django.contrib.auth import authenticate, login
from rest_framework.generics import CreateAPIView, ListCreateAPIView


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


class LoginViewSet(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(request.data)
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = UserSerializer(user)

            if serializer.is_valid():
                login(request, user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'message': 'invalid credentilas'}, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(CreateAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def create(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(data=user)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

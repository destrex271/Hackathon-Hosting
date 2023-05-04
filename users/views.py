from django.shortcuts import render
from rest_framework.exceptions import status
from rest_framework.views import APIView, Response

from users.models import CustomUser
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


class RegisterUser(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GetAllUsers(APIView):
    def get(self, request):
        data = UserSerializer(CustomUser.objects.all(), many=True)
        return Response(data.data, status = status.HTTP_200_OK)

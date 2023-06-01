from django.shortcuts import render
from datetime import datetime
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, UserSerializer


# Create your views here.
class LoginView(APIView):
    serializer_class = LoginSerializer

    def get(self, request):
        return Response({}, status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        if user is not None:
            user.last_login = datetime.now()
            user.save()
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status.HTTP_200_OK)
        else:
            return Response(
                {
                    "error": "401 Unathorized",
                    "message": "The credentials provided are not valid. Please review your information  and try again.",
                },
                status.HTTP_401_UNAUTHORIZED,
            )

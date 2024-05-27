from django.shortcuts import render
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from accounts.models import User, Profile
import requests
from django.contrib.auth import get_user_model

# within app imports
from accounts.serializers import(RegisterSerializer,
                                LoginSerializer,
                                ProfileSerializer
                                )
# third party imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

User = get_user_model()


# register

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        user.save()
        return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)


# login

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = LoginSerializer


# profile
class ProfileCreateView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
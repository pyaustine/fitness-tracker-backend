import unittest
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import User, Profile
from accounts.serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from accounts.views import RegisterView, MyTokenObtainPairView, ProfileCreateView, ProfileRetrieveUpdateView

class TestRegisterView(TestCase):
    def test_register_view(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post('/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

class TestMyTokenObtainPairView(TestCase):
    def test_login_view(self):
        user = User.objects.create_user('testuser', 'testuser@example.com', 'testpassword')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post('/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

class TestProfileCreateView(TestCase):
    def test_profile_create_view(self):
        user = User.objects.create_user('testuser', 'testuser@example.com', 'testpassword')
        token = self.client.post('/login/', {'username': 'testuser', 'password': 'testpassword'}, format='json').data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            'bio': 'Test bio'
        }
        response = self.client.post('/profile/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)

class TestProfileRetrieveUpdateView(TestCase):
    def test_profile_retrieve_view(self):
        user = User.objects.create_user('testuser', 'testuser@example.com', 'testpassword')
        profile = Profile.objects.create(user=user, bio='Test bio')
        token = self.client.post('/login/', {'username': 'testuser', 'password': 'testpassword'}, format='json').data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bio'], 'Test bio')

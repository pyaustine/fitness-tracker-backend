from django.urls import path
from . import views


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework import permissions


urlpatterns = [
    # auth
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('profile/', views.ProfileRetrieveUpdateView.as_view(), name='profile_view'),
    path('profile/create/', views.ProfileCreateView.as_view(), name='profile_create'),

]
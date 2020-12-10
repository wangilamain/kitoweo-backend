from django.urls import path, include, re_path
from knox import views as knox_views
from . import views
from rest_framework.routers import DefaultRouter
from . import views
from .views import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
userDetail = UserViewSet.as_view({
    'get': 'retrieve'
})
router = DefaultRouter()
router.register(r'Profile', ProfileViewSet)
router.register(r'User', UserViewSet)
urlpatterns = [
    path('', views.home, name='home'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/change-password/', ChangePasswordView.as_view(),
         name='change-password'),
    path('api/password_reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),

]
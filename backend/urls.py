from rest_framework.routers import DefaultRouter
from kitoweo.views import RegisterAPI
from django.urls import path, include
from knox import views as knox_views
from kitoweo.views import LoginAPI
from django.contrib import admin
from kitoweo.views import ProfileViewSet
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()

# router.register(r'profile', ProfileViewSet)
# router.register(r'user', UserViewSet)

urlpatterns = [
     path('admin/', admin.site.urls),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
      path('api/v1/', include(router.urls)),
]
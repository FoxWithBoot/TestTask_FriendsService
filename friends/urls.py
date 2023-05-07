from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FriendsViewSet, FriendshipViewSet, RegisterView  # , FriendsAPIView

router = DefaultRouter()
router.register(r'friends', FriendsViewSet, basename='friends')
router.register(r'friendship', FriendshipViewSet, basename='friendship')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]

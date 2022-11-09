from django.urls import path, include
from .views import UserViewSet, CustomerViewset
from rest_framework.routers import DefaultRouter
from rest_framework import routers

router = DefaultRouter()
router.register(r"customer", CustomerViewset, basename="customer")
router.register(r"user", UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls))
]
from django.urls import path
from .views import BlogViewSet, UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('users',UserViewSet,basename='users'),

router.register('',BlogViewSet,basename='blogs')

urlpatterns = router.urls



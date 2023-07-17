from django.urls import *
from rest_framework.routers import DefaultRouter
from .views import SongViewSet

router = DefaultRouter()
router.register('song', SongViewSet, basename='song')

urlpatterns = router.urls
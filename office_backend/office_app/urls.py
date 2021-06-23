from django.urls import path
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from .views import OfficeAPIView


router = SimpleRouter()
router.register(r'office/list', OfficeAPIView)


urlpatterns = router.urls
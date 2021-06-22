from django.urls import re_path, path
from .consumers import OfficeConsumer

ws_urlpatterns = [
    re_path(r'ws/offices/', OfficeConsumer.as_asgi())
]
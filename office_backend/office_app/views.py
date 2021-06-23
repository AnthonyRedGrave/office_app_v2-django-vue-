import re
from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

class OfficeAPIView(ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    
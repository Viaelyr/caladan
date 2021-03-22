from django.shortcuts import render
from rest_framework import viewsets

from .serializers import LittleSerializer
from .models import Little

# Create your views here.
class LittleViewSet(viewsets.ModelViewSet):
    queryset = Little.objects.all().order_by('name')
    serializer_class = LittleSerializer
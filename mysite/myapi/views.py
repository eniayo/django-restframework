from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import hero
from django.shortcuts import render

class heroViewSet(viewsets.ModelViewSet):
    queryset = hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

# Create your views here.

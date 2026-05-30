from django.shortcuts import render
from rest_framework import viewsets

from api.models import Company
from api.serializer import CompanySerializer

# Create your views here.
class CompanyViewsset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
from django.shortcuts import render
from rest_framework import viewsets

from api.models import Company, Employee
from api.serializer import CompanySerializer, EmployeeSerializer

# Create Company views here.
class CompanyViewsset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    

# Create Employee Views
class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

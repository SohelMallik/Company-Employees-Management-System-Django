from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import Response

from api import serializer
from api.models import Company, Employee
from api.serializer import CompanySerializer, EmployeeSerializer
# For Specific company employees
from rest_framework.decorators import action
from rest_framework.views import Response


# Create Company views here.
class CompanyViewsset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
    #companies/{pk}/employees/
    @action(detail=True, methods=['get'])
    def employees(self,request,pk=None):
        company=Company.objects.get(pk=pk)
        employees=Employee.objects.filter(company=company)
        emp_serializer=EmployeeSerializer(employees,many=True,context={'request':request})
        return Response(emp_serializer.data)
    

# Create Employee Views
class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

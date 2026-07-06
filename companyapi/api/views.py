from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import Response

from api import serializer
from api.models import Company, Employee
from api.serializer import CompanySerializer, EmployeeSerializer
# For Specific company employees
from rest_framework.decorators import action
from rest_framework.views import Response

#For Api Key Authentication
from rest_framework_api_key.permissions import HasAPIKey


# Create Company views here.
class CompanyViewsset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
    #For Api Key Authentication
    permission_classes=[HasAPIKey]
    
    #companies/{pk}/employees/
    @action(detail=True, methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            employees=Employee.objects.filter(company=company)
            serializer=EmployeeSerializer(employees,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)},status=400) 
    
        
    

# Create Employee Views
class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
     # Protect all Employee APIs
    permission_classes = [HasAPIKey]

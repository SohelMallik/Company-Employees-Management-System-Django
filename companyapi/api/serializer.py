#Create Serializer for company model
from rest_framework import serializers
from .models import Company, Employee

#Company Serializer
class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'
        
#Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):

    class Meta: #Store meta class
        model = Employee
        fields = '__all__'
        
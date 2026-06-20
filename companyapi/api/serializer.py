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
    company = serializers.CharField(source='company.__str__', read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
        
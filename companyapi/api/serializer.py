#Create Serializer for company model
from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


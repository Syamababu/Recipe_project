from rest_framework import serializers
from apiapp.models import Company , Employee

class comapnyserializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'

class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
from rest_framework import serializers
from .models import employee
from .models import department

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['id','fname','lname','emp_sal','email']

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = ['id','dept_name','dept_id','dept_budget','dept_employees']
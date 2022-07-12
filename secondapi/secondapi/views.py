from .models import employee
from .models import department
from .serializers import departmentSerializer, employeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

class org1ViewSet(ViewSet):
    def list(self,request):
        employees=employee.objects.all()
        serializer = employeeSerializer(employees, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer=employeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def retrieve(self,request,pk):
        try:
            employee_info=employee.objects.get(pk=pk)
        except employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=employeeSerializer(employee_info)
        return Response(serializer.data)

    def update(self,request,pk):
        try:
            employee_info=employee.objects.get(pk=pk)
        except employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = employeeSerializer(employee_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        try:
            employee_info=employee.objects.get(pk=pk)
        except employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class org2ViewSet(ViewSet):
    def list(self,request):
        depart=department.objects.all()
        serializer = departmentSerializer(depart, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer=departmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def retrieve(self,request,pk):
        try:
            depart_info=department.objects.get(pk=pk)
        except department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=departmentSerializer(depart_info)
        return Response(serializer.data)

    def update(self,request,pk):
        try:
            depart_info=department.objects.get(pk=pk)
        except department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = departmentSerializer(depart_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        try:
            depart_info=department.objects.get(pk=pk)
        except department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        depart_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
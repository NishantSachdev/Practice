
from .models import employee
from .serializers import employeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# get full info or post new info
@api_view(['GET','POST'])
def employee_list(request):

    # get all employee objects info, serialize them, return response 
    if request.method=='GET':
        employees=employee.objects.all()
        serializer = employeeSerializer(employees, many=True)
        return Response(serializer.data)

    # get input for emp info, serialize it, add new object and return response showing newly added object
    if request.method=='POST':
        serializer=employeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# get particular info from id, update info for a particular object, delete a particular object
@api_view(['GET','PUT','DELETE'])
def employee_detail(request, id):

    # check to see if the request is valid
    try:
        employee_info=employee.objects.get(pk=id)
    except employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get info for specific object 
    if request.method == 'GET':
        serializer=employeeSerializer(employee_info)
        return Response(serializer.data)

    # update info for specific object 
    elif request.method == 'PUT':
        serializer = employeeSerializer(employee_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete specific object 
    elif request.method == 'DELETE':
        employee_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


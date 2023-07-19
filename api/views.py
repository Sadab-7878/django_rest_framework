from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):

        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
            return Response(emps_serializer.data)

        except Exception as e:
            print(e)
            return Response({'message': 'Employee does not exist'})
        
    @action(detail=True, methods=['get'], url_path='employees/(?P<employee_pk>[^/.]+)')
    def employee(self, request, pk=None, employee_pk=None):
        try:
            company = Company.objects.get(pk=pk)
            employee = Employee.objects.get(pk=employee_pk, company=company)
            emp_serializer = EmployeeSerializer(employee, context={'request': request})
            return Response(emp_serializer.data)

        except Company.DoesNotExist:
            return Response({'message': 'Company does not exist'})

        except Employee.DoesNotExist:
            return Response({'message': 'Employee does not exist'})

        except Exception as e:
            print(e)
            return Response({'message': 'An error occurred'})
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
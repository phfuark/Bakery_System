from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

@api_view(['GET'])
def get_employee_by_id(req, pk):
    if req.method == 'POST':
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee_serializer = EmployeeSerializer(employee, data=req.data)
        return Response(employee_serializer, status=status.HTTP_200_OK)
        
@api_view(['GET'])
def get_product_by_id(req, pk):
    if req.method == 'POST':
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product_serializer = productSerializer(product, data=req.data)
        return Response(product_serializer, status=status.HTTP_200_OK)
        
@api_view(['GET'])
def get_employee_by_id(req, pk):
    if req.method == 'POST':
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee_serializer = EmployeeSerializer(employee, data=req.data)
        return Response(employee_serializer, status=status.HTTP_200_OK)
        
@api_view(['GET'])
def get_employee_by_id(req, pk):
    if req.method == 'POST':
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee_serializer = EmployeeSerializer(employee, data=req.data)
        return Response(employee_serializer, status=status.HTTP_200_OK)
        
@api_view(['GET'])
def get_employee_by_id(req, pk):
    if req.method == 'POST':
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee_serializer = EmployeeSerializer(employee, data=req.data)
        return Response(employee_serializer, status=status.HTTP_200_OK)
        
        
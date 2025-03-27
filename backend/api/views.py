from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

# GET =====================================================================

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
        product_serializer = ProductSerializer(product, data=req.data)
        return Response(product_serializer, status=status.HTTP_200_OK)
        
@api_view(['GET'])
def get_card_by_id(req, pk):
    if req.method == 'POST':
        try:
            card = Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        card_serializer = CardSerializer(card, data=req.data)
        return Response(card_serializer, status=status.HTTP_200_OK)
        
@api_view(['GET'])
def get_supplier_by_id(req, pk):
    if req.method == 'POST':
        try:
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        supplier_serializer = SupplierSerializer(supplier, data=req.data)
        return Response(supplier_serializer, status=status.HTTP_200_OK)
    
# GET =====================================================================



# POST ====================================================================

@api_view(["POST"])
def create_employee(request):
    employee_serializer = EmployeeSerializer(data=request.data)
    if employee_serializer.is_valid():
        employee_serializer.save()
        return Response(employee_serializer.data, status=status.HTTP_201_CREATED)
    return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_card(request):
    card_serializer = CardSerializer(data=request.data)
    if card_serializer.is_valid():
        card_serializer.save()
        return Response(card_serializer.data, status=status.HTTP_201_CREATED)
    return Response(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_product(request):
    product_serializer = ProductSerializer(data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)
    return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_supplier(request):
    supplier_serializer = SupplierSerializer(data=request.data)
    if supplier_serializer.is_valid():
        supplier_serializer.save()
        return Response(supplier_serializer.data, status=status.HTTP_201_CREATED)
    return Response(supplier_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST ====================================================================


# PUT ====================================================================

@api_view(['PUT'])
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee_serializer = EmployeeSerializer(employee, data=request.data)
    if employee_serializer.is_valid():
        employee_serializer.save()
        return Response(employee_serializer.data, status=status.HTTP_200_OK)
    return Response(employee_serializer.errors, status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)

@api_view(['PUT'])
def update_card(request, pk):
    card = get_object_or_404(card, pk=pk)
    card_serializer = CardSerializer(card, data=request.data)
    if card_serializer.is_valid():
        card_serializer.save()
        return Response(card_serializer.data, status=status.HTTP_200_OK)
    return Response(card_serializer.errors, status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)

@api_view(['PUT'])
def update_product(request, pk):
    product = get_object_or_404(product, pk=pk)
    product_serializer = ProductSerializer(product, data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_200_OK)
    return Response(product_serializer.errors, status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)

@api_view(['PUT'])
def update_supplier(request, pk):
    supplier = get_object_or_404(supplier, pk=pk)
    supplier_serializer = SupplierSerializer(supplier, data=request.data)
    if supplier_serializer.is_valid():
        supplier_serializer.save()
        return Response(supplier_serializer.data, status=status.HTTP_200_OK)
    return Response(supplier_serializer.errors, status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
    

# PUT ====================================================================

# DELETE ====================================================================

@api_view(['DELETE'])
def delete_employee(request, pk):
    employee = get_object_or_404(employee, pk=pk)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_card(request, pk):
    card = get_object_or_404(card, pk=pk)
    card.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_product(request, pk):
    product = get_object_or_404(product, pk=pk)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_supplier(request, pk):
    supplier = get_object_or_404(supplier, pk=pk)
    supplier.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# DELETE ====================================================================
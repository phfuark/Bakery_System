from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

@api_view(['GET'])
def get_employee_by_id(req, pk):
    if req.method == 'POST':
        

        
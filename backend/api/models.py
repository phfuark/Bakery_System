from django.db import models

choicesEmployee = ['Attendant', 'Baker', 'Cleaner']

class Employee(models.Model):
    id_employee = models.PositiveIntegerField(primary_key=True)
    function = models.TextChoices(choicesEmployee)

class Card(models.Model):
    id_card = models.PositiveIntegerField(primary_key=True)

class Product(models.Model):
    id_product = models.PositiveIntegerField(primary_key=True)    
    name = models.CharField(max_length=100, primary_key=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Supplier(models.Model):
    id_supplier = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    adress = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)


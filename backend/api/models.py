from django.db import models

class Employee(models.Model):
    class FunctionChoices(models.TextChoices):
        ATTENDANT = 'Attendant'
        BAKER = 'Baker'
        CLEANER = 'Cleaner'

    id_employee = models.AutoField(primary_key=True)
    function = models.CharField(max_length=20, choices=FunctionChoices.choices)

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Card(models.Model):
    id_card = models.AutoField(primary_key=True)
    product = models.ManyToManyField(Product)

class Supplier(models.Model):
    id_supplier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)

class Sale(models.Model):
    id_sale = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="sales")

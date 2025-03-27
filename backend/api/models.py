from django.db import models



class Employee(models.Model):
    function = models.CharField()
    #  Negócio na moral
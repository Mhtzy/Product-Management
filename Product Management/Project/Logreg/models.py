
from unittest.util import _MAX_LENGTH
from django.db import models

class Company(models.Model):
    Company_ID=models.AutoField(primary_key=True )
    Company_Name=models.CharField(max_length=100, unique=True)
    Email=models.EmailField(max_length=30)

    def __str__(self):
        return self.Company_Name





class User(models.Model):
    Company_Name=models.CharField(max_length=10)
    Username=models.CharField(max_length=100 , unique=True)
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=30)

    def __str__(self):
        return self.Username

class Pro(models.Model):
    Product_ID=models.AutoField(primary_key=True)
    Product_Name=models.CharField(max_length=30, unique=True)
    Warranty=models.CharField(max_length=30)

    def __str__(self):
        return self.Product_Name

class Itm(models.Model):
    Product_Name=models.CharField(max_length=30)
    Item_ID=models.AutoField(primary_key=True)
    Item_Name=models.CharField(max_length=30)

    def __str__(self):
        return self.Item_Name

class Inv(models.Model):
    Product_Name=models.CharField(max_length=30)
    Item_Name=models.CharField(max_length=30)
    Stock=models.IntegerField()

    def __str__(self):
        return self.Item_Name
    



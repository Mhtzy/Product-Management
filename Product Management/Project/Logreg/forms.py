

from django import forms

from .models import Company,Pro,Itm

class Company_Registration(forms.Form):
    Company_Name=forms.CharField()
    Email=forms.EmailField()

tup =Company.objects.values_list('Company_Name',flat=True)
li = []
for i in tup:
    li.append(i)


b=[]
c=[]
for i in range(0,len(li)):
    b.append(li[i])
    b.append(li[i])
    c.append(b)
    b=[]
lis = []
for i in range(0, len(c)):
    e=tuple(c[i])
    lis.append(e)

tu=tuple(lis)

class User_Registration(forms.Form):
    Company_Name=forms.ChoiceField(choices=tu)
    Username=forms.CharField()
    Email=forms.EmailField()
    Password=forms.CharField()

class Login(forms.Form):
    Username=forms.CharField()
    Password=forms.CharField()

class Product(forms.Form):
    Product_Name=forms.CharField()
    Warranty=forms.CharField()
    

l =Pro.objects.values_list('Product_Name',flat=True)
li = []
for i in l:
    li.append(i)


b=[]
c=[]
for i in range(0,len(li)):
    b.append(li[i])
    b.append(li[i])
    c.append(b)
    b=[]
lis = []
for i in range(0, len(c)):
    e=tuple(c[i])
    lis.append(e)

lst=tuple(lis)
class Item(forms.Form):
    Product_Name=forms.ChoiceField(choices=lst)
    Item_Name=forms.CharField()

l =Itm.objects.values_list('Item_Name',flat=True)
li = []
for i in l:
    li.append(i)


b=[]
c=[]
for i in range(0,len(li)):
    b.append(li[i])
    b.append(li[i])
    c.append(b)
    b=[]
lis = []
for i in range(0, len(c)):
    e=tuple(c[i])
    lis.append(e)

ls=tuple(lis)
class Inventory(forms.Form):
    Product_Name=forms.ChoiceField(choices=lst)
    Item_Name=forms.ChoiceField(choices=ls)
    Stock=forms.IntegerField()




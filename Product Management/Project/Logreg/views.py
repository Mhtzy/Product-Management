from sre_constants import IN
from telnetlib import AUTHENTICATION
from django.shortcuts import render
from django.http   import HttpResponseRedirect

from .models import User,Company,Pro,Itm,Inv
from .forms import User_Registration,Company_Registration, Login,Product,Item,Inventory
from django.contrib.auth import authenticate

def Companyregistration(request):
    fm=Company_Registration
    
    usr=False
    if request.method=="POST":
        fm=Company_Registration(request.POST)
        if fm.is_valid():
            cn=fm.cleaned_data.get('Company_Name')
            em=fm.cleaned_data.get('Email')
            if Company.objects.filter(Company_Name=cn).exists():
                usr=True
                return render(request , 'company.html', {'form':fm ,'usr':usr})
            else:
                reg=Company(Company_Name=cn,Email=em)
                reg.save()
                return render(request ,'company_success.html')           

    else:
        return render(request , 'company.html', {'form':fm,'usr':usr})
    

def Userregistration(request):
    fm=User_Registration
    usr=False
    if request.method=="POST":
        fm=User_Registration(request.POST)
        error=fm.errors
        print(error)
        if fm.is_valid():
            cn=fm.cleaned_data.get('Company_Name')
            un=fm.cleaned_data.get('Username')
            
            em=fm.cleaned_data.get('Email')
            pwd=fm.cleaned_data.get('Password')
            if User.objects.filter(Username=un).exists():

                usr=True
                return render(request , 'user.html', {'form':fm ,'usr':usr})
            else:
            
                reg=User(Company_Name=cn,Username=un,Email=em,Password=pwd)
                reg.save()
                return render(request , 'user_success.html')  
             

    else:
        return render(request , 'user.html', {'form':fm,'usr':usr})
    

def login(request):
    fm=Login
    usr=False
    use=False
    if request.method=="POST":
        fm=Login(request.POST)
        
        if fm.is_valid():
            un=fm.cleaned_data.get('Username')
            pwd=fm.cleaned_data.get('Password')
            # user = authenticate(Username=un,Password=pwd)

            if User.objects.filter(Username=un).exists():
                # login(request, users_validation, backend=settings.AUTHENTICATION_BACKENDS[0])
                if User.objects.filter(Username=un, Password=pwd).exists():
                                      
                    return HttpResponseRedirect('/Logreg/login/login_success/')
                else:
                    use=True
                    return render(request , 'login.html',{'form':fm ,'use':use})
            else:
                usr=True
                return render(request , 'login.html',{'form':fm ,'usr':usr})
    else: 
        return render(request, 'login.html', {'form':fm, 'usr':usr})
    
def login_success(request):
    return render(request , 'login_success.html')

def addprod(request):
    fm=Product
    ur=False
    
    if request.method=="POST":
        fm=Product(request.POST)
        usr=False
        if fm.is_valid():
            p=fm.cleaned_data.get('Product_Name')
            w=fm.cleaned_data.get('Warranty')
            if Pro.objects.filter(Product_Name=p).exists():
                ur=True
                return render(request, 'addproduct.html', {'form':fm,'ur':ur} )
            else:
                reg=Pro(Product_Name=p,Warranty=w)
                reg.save()
                usr=True
                fm=Product
                return render(request, 'addproduct.html', {'form':fm,'usr':usr} )

    else:
        return render(request,"addproduct.html",{'form':fm})

def viewprod(request):
    prod=Pro.objects.all()
    return render(request,"viewproduct.html",{'prod':prod})

def additem(request):
    fm=Item
    usr=False 
    if request.method=="POST":
        fm=Item(request.POST)
        if fm.is_valid():
            pn=fm.cleaned_data.get("Product_Name")
            id=fm.cleaned_data.get("Item_ID")
            ina=fm.cleaned_data.get("Item_Name")
            reg=Itm(Product_Name=pn,Item_ID=id,Item_Name=ina)
            reg.save()
            usr=True
            fm=Item
            return render(request,'additem.html',{'form':fm,'usr':usr})

        
    else:        
        return render(request,"additem.html" ,{'form':fm})

def viewitem(request):
    itms=Itm.objects.all()
    return render(request,"viewitem.html",{'itms':itms})

def delete_prod(request,Product_ID):
    if request.method=="POST":
        pro=Pro.objects.get(pk=Product_ID)
        pro.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_itm(request,Item_ID):

    if request.method=="POST":
        pro=Itm.objects.get(pk=Item_ID)
        pro.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def addinventory(request):
    fm=Inventory
    usr=False 
    ur=False
    if request.method=="POST":
        fm=Inventory(request.POST)
        if fm.is_valid():
            pn=fm.cleaned_data.get("Product_Name")
            id=fm.cleaned_data.get("Item_Name")
            ina=fm.cleaned_data.get("Stock")
            
            if Itm.objects.filter(Product_Name=pn, Item_Name=id).exists():
                reg=Inv(Product_Name=pn,Item_Name=id,Stock=ina)
                reg.save()
                usr=True
                fm=Inventory
                return render(request,'addinventory.html',{'form':fm,'usr':usr})
            else:
                ur=True
                return render(request,"addinventory.html" ,{'form':fm,'ur':ur})

        
    else:        
        return render(request,"addinventory.html" ,{'form':fm})
    

def viewinventory(request):
    
    itms=Inv.objects.all()
    return render(request,"viewinventory.html",{'itms':itms})
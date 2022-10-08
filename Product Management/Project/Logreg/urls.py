
from django.urls import path

from . import views

urlpatterns = [
    
    path('Companyregistration/',views.Companyregistration),
    path('Userregistration/', views.Userregistration),
    path('login/',views.login),
    path('login/login_success/addproduct/',views.addprod),
    path('login/login_success/viewproduct/',views.viewprod),
    path('login/login_success/viewproduct/deleteprod/<int:Product_ID>/',views.delete_prod , name="deleteproduct"),
    path('login/login_success/additem/',views.additem),
    path('login/login_success/viewitem/',views.viewitem),
    path('login/login_success/viewproduct/deleteitm/<int:Item_ID>/',views.delete_itm , name="deleteitem"),
    path('login/login_success/addinventory/',views.addinventory),
    path('login/login_success/viewinventory/',views.viewinventory),
    path('login/login_success/',views.login_success)
]
"""ac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about),
    path('products/', views.products),
    path('checkout/', views.checkout,name='checkout'),
    path('product-single/<int:pid>/', views.productsingle,name='productsingle'),
    path('add_to_cart/<int:pid>/', views.add_to_cart,name='add_to_cart'),
    path('update_quantity/<int:cart_id>/', views.update_quantity,name='update_quantity'),
    path('remove_quantity/<int:cart_id>/', views.remove_quantity,name='remove_quantity'),
    path('delete_cart/<int:cart_id>/', views.delete_cart,name='delete_cart'),
    
    path('buy_now/<int:pid>/', views.buy_now,name='buy_now'),
    path('payment/', views.payment),
    path('contact/', views.contact),
    path('login/', views.login,name='login'),
    path('logout/', views.user_logout,name='logout')

    

    
    
    
    
    
    
] 

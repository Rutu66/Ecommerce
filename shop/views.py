from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login as l 

def index(request):
    productdata = product.objects.all()
    return render(request, 'index.html',locals())

def about(request):
    return render(request, 'about.html')

def products(request):
    productdata = product.objects.all()
    # if request.method=="GET":
    #     pd=request.GET.get('search')
    #     if pd!=None:
    #         productdata = product.objects.filter(product_name__icontains=pd)
    data = {
        'productdata':productdata
    }
    return render(request, 'products.html',data)

def productsingle(request,pid):

    productsingle = product.objects.filter(product_id=pid)
    data = {
        'productsingle':productsingle
    }
    return render(request, 'product-single.html',data)

def add_to_cart(request, pid):
    products = get_object_or_404(product, product_id=pid)
    
    # Assuming 'cart' is a list in the session to store product IDs
    carts = cart.objects.filter(user=request.user,product=products).first()
    if carts:
        messages.info(request, "Already in ")
    else:
        cart(user=request.user,product=products).save()
        messages.info(request, 'Added in cart')
    
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def buy_now(request, pid):
    products = get_object_or_404(product, product_id=pid)
     
    # Assuming 'cart' is a list in the session to store product IDs
    carts = cart.objects.filter(user=request.user,product=products).first()
    if carts:
        return redirect('checkout')
    else:
        cart(user=request.user,product=products).save()
    
        return redirect('checkout')

def checkout(request):
    cart_obj = cart.objects.all()
    cart_items = cart.objects.filter(user=request.user)
    amount = 0
    for i in cart_items:
        value = i.product.price*i.quantity
        amount = value+amount
        
    total = amount
    data={
        'cart':cart_obj,
        'total':total
        
    }
    return render(request, 'checkout.html',data)

def update_quantity(request, cart_id):
    carts = cart.objects.get(id=cart_id)
    carts.quantity += 1
    carts.save()
    return redirect('checkout')

def remove_quantity(request, cart_id):
    carts = cart.objects.get(id=cart_id)
    carts.quantity -= 1
    carts.save()
    return redirect('checkout')

def delete_cart(request, cart_id):
    carts = cart.objects.get(id=cart_id)
    carts.delete()
    return redirect('checkout')

def order_place(request):
    carts = cart.objects.filter(user=request.user)
    for i in carts:
        order.objects.create(user=request.user,product=i.product, quantity = i.quantity)
    carts.delete()
    return redirect('index')
    

def orders(request):
    order_obj = order.objects.filter(user=request.user)
    
    
    return render(request, 'order.html',locals())
    


def login(request):
    
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            l(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html')
        
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('index')
    






def payment(request):
    return render(request, 'payment.html')

def contact(request):
    return render(request, 'contact.html')

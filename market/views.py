from django.shortcuts import render
from. models import Product

def home (request):
    return render(request, 'home.html')

def product_list (request):
    products=Product.objects.all()   
    return render(request, 'list.html', {'products': products})
    

def order_name(request):
    products= Product.objects.order_by('name')
    return render(request, 'list.html', {'products': products})

def lowest_price(request):
    products= Product.objects.order_by('value')
    return render(request, 'list.html', {'products': products})


def biggest_price(request):
    products= Product.objects.order_by('-value')
    return render(request, 'list.html', {'products': products})

    
# Create your views here.

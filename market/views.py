from django.shortcuts import render, redirect
from. models import Product

def home (request):
    number=request.session.get('number', 1)
    request.session['number']=number +1
    return render(request, 'home.html' )

  
def product_list (request):
    if (request.method == 'POST'):
        pes = request.POST.get('pes')
        if (pes == "cres"):
            products=Product.objects.order_by('name')
            return render(request, 'list.html/', {'products':products})
        elif (pes == "decres"):
            products=Product.objects.order_by('-name')
            return render(request, 'list.html/', {'products':products})
        elif(pes == "maior"):
            products=Product.objects.order_by('-value')
            return render(request, 'list.html/', {'products':products})
        elif(pes == "menor"):
            products=Product.objects.order_by('value')
            return render(request, 'list.html/', {'products':products})
    else:
        products = Product.objects.all()
        return render(request, 'list.html/', {'products':products})

def purchase (request, product_id):
    product= Product.objects.get(pk=product_id)
    l = request.session.get('li', [])
    l.append(product.id)
    request.session['li']= l
    return redirect('/market/list/')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
def product_show (request):
    l = request.session['li']
    products=[]
    for product_id in l:
        product= Product.objects.get(pk=product_id)
        products.append(product)
    return render(request, 'show.html/', {'product': product})
       


     


    
    
    
    

    







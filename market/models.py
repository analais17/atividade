from django.db import models




class Product (models.Model):
    name = models.CharField(max_length=50)
    value= models.CharField(max_length=11)
  
       

class Client(models.Model):
    name = models.CharField(max_length=50)
    cpf= models.CharField(max_length=10)
    
    

class Shopping_Cart(models.Model):
    purchase_date=models.CharField(max_length=50)
    client=models.ForeignKey(Client, on_delete=models.CASCADE) 
   
  

class Amount (models.Model):
    amount=models.CharField(max_length=50)
    product=models.ForeignKey(Product, on_delete=models.CASCADE) 
    shopping_cart=models.ForeignKey(Shopping_Cart, on_delete=models.CASCADE,primary_key=True) 

# Create your models here.

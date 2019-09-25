from.import views
from django.urls import path 

urlpatterns = [
    path('', views.home),
    path('list/',views.product_list),
    path('ordername/',views.order_name),
    path('smaller/',views.lowest_price),
    path('bigger/',views.biggest_price)


    
]

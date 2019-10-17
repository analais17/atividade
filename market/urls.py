from.import views
from django.urls import path 

urlpatterns = [
    path('', views.home),
    path('list/',views.product_list),
    path('<int:product_id>/', views.purchase),
    path('show/', views.product_show)

    

    
]

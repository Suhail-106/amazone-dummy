from django.urls import path
from Fashion import views

urlpatterns = [
    path('', views.vocalforlocal13, name="vocalforlocal"),


   path('product_details/<str:product_type>/<int:product_id>',views.product_details_dynamic,name="product_details_dynamic"),
   path('product_add_to_cart/<str:product_type>/<int:product_id>',views.add_to_cart_dynamic,name="Fashion_add_to_cart_dynamic"),
   path('product_buy_now/<str:product_type>/<int:product_id>',views.buy_now_dynamic,name="Fashion_buy_now_dynamic"),






]

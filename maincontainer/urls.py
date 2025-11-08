from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
 
    path('add-to-cart/<int:product_id>/<str:which_content>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),

    #-----------------------------------bestseller of watch---------------------------------------
    path('products/', views.filtered_products, name='filtered_products'),
  
   #------------------------------------remove from cart.html urls-------------------------------
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

   #---------------------------------------mobilepage-----------------------------
    path('mobile/', views.mobilepage, name="mobile"),
   
    #------------------------------------electronics page----------------------------

    path('electronics/', views.electronics, name="electronics"),
  
    path('autoupdate/',views.autoupdatedataandimage,name="autoupdatedataandimage"),

    #-------------------------------------form urls------------------------------------------
    path('form/',views.form,name="form"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('verify_otp/', views.verify_otp, name="verify_otp"),

    #-------------------------------------product details in index.html-------------------------------------
    path('product/<int:product_id>/<str:which_content>/', views.product_detail, name='product_detail'),

   

    #--------------------------freshpage ------------------------------
    path('Fresh/', views.fresh, name="fresh"),
   
   #----------------------------------funcion for product buy to paymentsuccess----------------------
    path("add-address/", views.add_address, name="add_address"),


    path('buy-now/<int:product_id>/<str:which_content>/', views.buy_now, name='buy_now'),

    path('payment-success/', views.payment_success, name="payment_success"),



   path('product/<str:product_type>/<int:product_id>/', views.product_detail_dynamic, name='product_detail_dynamic'),
   path('add-to-cart/<str:product_type>/<int:product_id>/', views.add_to_cart_dynamic, name='add_to_cart_dynamic'),
   path('buy-now/<str:product_type>/<int:product_id>/', views.buy_now_dynamic, name='buy_now_dynamic'),

]

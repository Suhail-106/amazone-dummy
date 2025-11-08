from django.urls import path
from . import views

urlpatterns = [
    path('',views.homekitchen, name="home&kitchen"),
   

]

from django.urls import path
from . import views
from maincontainer import views as main_views 


urlpatterns = [
    path('', views.allcontent, name="New_Releases"),
        
]

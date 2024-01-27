# myapp/urls.py
from django.urls import path
from .views import item_list
from .views import home, about

urlpatterns = [
    
    path('', item_list, name='item_list'),  
    path('home/',home,name='home'),
    path('about/',about,name='about'),
]

from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()
    context = {'items': items, 'user': request.user}
    return render(request, 'item_list.html', {'items': items})

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

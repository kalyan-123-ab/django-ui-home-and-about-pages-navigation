# projectapp/views.py
from django.shortcuts import render

def index(request):
    # your view logic here
    return render(request, 'projectapp/your_template.html')


def home(request):
    return render(request, 'other_template.html')

# # views.py
# from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

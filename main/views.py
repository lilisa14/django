from django.shortcuts import render
from .models import Task


def index(request):
    return render(request, 'main/index.html')

def about(request):
    tasks = Task.objects.all()
    return render(request, 'main/about.html', {'tasks': tasks})

def list(request):
    return render(request, 'main/list.html')

def mmain(request):
    return render(request, 'main/mmain.html')
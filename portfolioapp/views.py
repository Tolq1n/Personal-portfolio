from django.shortcuts import render
from .models import Projects


def home(request):
    projects = Projects.objects.all()
    return render(request, 'home.html', {'projects':projects})

def about(request):
    return render(request, 'about.html')

def work(request):
    projects = Projects.objects.all()
    return render(request, 'work.html', {'projects':projects})

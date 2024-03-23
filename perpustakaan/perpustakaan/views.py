from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def mia(request):
    return render(request, 'mia.html')
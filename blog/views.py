from django.shortcuts import render
from django.http import HttpResponse

def authors(request):
    return render(request, 'blog/autores.html')

def blog(request):
    return render(request, 'blog/index.html')

def exemplo(request):
    return render(request, 'blog/exemplo.html')

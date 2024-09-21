from django.shortcuts import render

from django.http import HttpResponse

def sobre(request):
    return render(request, 'sobre.html')

def trabalhe_conosco(request):
    return render(request, 'trabalhe_conosco.html')
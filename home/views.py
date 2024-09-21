from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html') 

def trabalhe_conosco(request):
    return HttpResponse("TRABALHE CONOSCO HOMEVIEWS")

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"homepage.html")

def error_404(request,exception):
    data = {}
    return render(request,"error404.html",data)
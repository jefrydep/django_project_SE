from django.shortcuts import render
from servicios.models import Servicio

# from django.http import HttpResponse

# Create your views here.

# def blog(request):
#     return render(request,'home.html')

def home(request):
    return render(request,'home.html')

def blog(request):
    return render(request,'blog.html')

def contacto(request):
    return render(request,'contacto.html')


def servicios(request):
    # title= 'Django Jefry'
    servicios = Servicio.objects.all()
    print(servicios)
    return render(request,'servicios.html',{
        # 'title':title
   
    'servicios':servicios
   
    })

def tienda(request):
    return render (request,'tienda.html')
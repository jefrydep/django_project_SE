from django.shortcuts import render

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
    title= 'Django Jefry'
    return render(request,'servicios.html',{
        'title':title
    })

def tienda(request):
    return render (request,'tienda.html')
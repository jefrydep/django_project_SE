from django.urls import path
from . import views
urlpatterns =[
    path('blog/',views.blog),
    path('contacto/',views.contacto),
    path('home/',views.home),
    path('servicios/',views.servicios),
    path('tienda/',views.tienda),
]
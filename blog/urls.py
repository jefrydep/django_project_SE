from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    path('blog/',views.blog),
    path('contacto/',views.contacto),
    path('home/',views.home),
    path('servicios/',views.servicios),
    path('tienda/',views.tienda),
]
urlpatterns=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
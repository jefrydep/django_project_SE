from django.contrib import admin
# aqui registramos nuestros modelos
from .models import Servicio
# Register your models here.
class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields=('Created','Updated')
admin.site.register(Servicio)
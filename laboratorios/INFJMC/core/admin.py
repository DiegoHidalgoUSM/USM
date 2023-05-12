from django.contrib import admin

# Register your models here.
from core.models import carrera,docente

class CarreraAdmin (admin.ModelAdmin):
    pass

admin.site.register(carrera,CarreraAdmin)

class DocenteAdmin (admin.ModelAdmin):
    pass

admin.site.register(docente,DocenteAdmin)
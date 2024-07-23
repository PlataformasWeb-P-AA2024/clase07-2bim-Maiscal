from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Edificio, Departamento

class EdificioAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    list_filter = ('tipo',)


admin.site.register(Edificio, EdificioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'costo', 'nCuartos', 'edificio')
    # se agrega el atributo 
    # raw_id_fields que permite acceder a una interfaz 
    # para buscar los estudiantes y seleccionar el que 
    # se desee
    raw_id_fields = ('edificio',)

admin.site.register(Departamento, DepartamentoAdmin)
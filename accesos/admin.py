from django.contrib import admin
from .models import Acceso, Area, SecAcc, Seccion, ArSecc,persona, cargo, CarAcc
from import_export import  fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export.fields import Field
# Register your models here.

admin.site.site_header = "Sistema de Accesos Industrias Cabrera"
admin.site.site_title = "Sistema de Accesos"
admin.site.index_title = "Bienvenidos al portal de administración"

@admin.register(Acceso)
class AccesoAdmin(admin.ModelAdmin):
    list_display = ('Acceso',)
    search_fields = ['Acceso', ]
    ordering = ['id']
    

class ArSeccInline(admin.TabularInline):
    model = ArSecc
    extra = 1
    

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('Area',) 
    inlines = [ArSeccInline]
    ordering = ['id']
    

#@admin.register(Secc_Acc)
class SecAccInline(admin.TabularInline):
    model = SecAcc
    extra = 1
    

@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)
    inlines = [SecAccInline]
    search_fields = ['Nombre', ]
    ordering = ['id']

  

@admin.register(persona)
class personaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre','apellido','usr','cargo','fechaIngreso','fechaRetiro')
    search_fields = ['nombre','apellido' ]


class CarAccInline(admin.TabularInline):
    model = CarAcc
    extra = 1
    autocomplete_fields = ['Acceso']
    
class BookResource(resources.ModelResource):
    accesos = fields.Field(
        column_name='accesos',
        attribute='accesos',
        widget=ManyToManyWidget(Acceso, field='Acceso',separator=','))
    class Meta:
        model = cargo
        fields = ('cargo','accesos')    

@admin.register(cargo)
class cargoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('cargo',)
    inlines = [CarAccInline]
    search_fields = ['Cargo', ]
    resource_class = BookResource
    


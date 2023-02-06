from django.contrib import admin
from .models import Acceso, Area, SecAcc, Seccion, ArSecc,persona, cargo, CarAcc
# Register your models here.

admin.site.site_header = "Sistema de Accesos Industrias Cabrera"
admin.site.site_title = "Sistema de Accesos"
admin.site.index_title = "Bienvenidos al portal de administración"

@admin.register(Acceso)
class AccesoAdmin(admin.ModelAdmin):
    list_display = ('Acceso',)

class ArSeccInline(admin.TabularInline):
    model = ArSecc
    extra = 1

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('Area',) 
    inlines = [ArSeccInline]

#@admin.register(Secc_Acc)
class SecAccInline(admin.TabularInline):
    model = SecAcc
    extra = 1
    

@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)
    inlines = [SecAccInline]

@admin.register(persona)
class personaAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','usr','cargo','fechaIngreso','fechaRetiro')

class CarAccInline(admin.TabularInline):
    model = CarAcc
    extra = 1

@admin.register(cargo)
class cargoAdmin(admin.ModelAdmin):
    list_display = ('cargo',)
    inlines = [CarAccInline]
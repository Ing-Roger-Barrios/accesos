from django.contrib import admin
from .models import Acceso, Area, SecAcc, Seccion, ArSecc
# Register your models here.


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
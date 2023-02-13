from django.db import models
import uuid
# Create your models here.




class Acceso(models.Model):
    Acceso = models.CharField(max_length=200, verbose_name='Acceso',default='')

    def __str__(self):
        return self.Acceso
    class Meta:
        verbose_name_plural = "3.- Acceso"


class Seccion(models.Model):
    Nombre = models.CharField(max_length=200, verbose_name='Seccion',default='')
    accesos = models.ManyToManyField(Acceso, through='SecAcc', blank=True,)

    def __str__(self):
        return self.Nombre
    class Meta:
        verbose_name_plural = "2.- Seccion"

class SecAcc(models.Model):
    Seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    Acceso = models.ForeignKey(Acceso, on_delete=models.CASCADE)
    

class Area(models.Model):
    Area = models.CharField(max_length=200, verbose_name='Area',default='')
    Seccion = models.ManyToManyField(Seccion, through='ArSecc', blank=True,)
    
    def __str__(self):
        return self.Area
    class Meta:
        verbose_name_plural = "1.- Area"

class ArSecc(models.Model):
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)
    Seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "ArSecc"

class cargo(models.Model):
    cargo = models.CharField(max_length=200, verbose_name='Cargo', default='')
    accesos = models.ManyToManyField(Acceso, through='CarAcc', blank=True,)

    def __str__(self):
        return self.cargo

class persona(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre', default='')
    apellido = models.CharField(max_length=200, verbose_name='Apellido', default='')
    usr = models.CharField(max_length=10, verbose_name='Usuario', default='')
    cargo = models.ForeignKey(cargo, on_delete=models.CASCADE)
    fechaIngreso = models.DateField(verbose_name='Fecha de Ingreso', blank=True, null=True)
    fechaRetiro = models.DateField(verbose_name='Fecha de Retiro', blank=True, null=True)

    def __str__(self):
        return self.nombre



class CarAcc(models.Model):
    cargo = models.ForeignKey(cargo, on_delete=models.CASCADE)
    Acceso = models.ForeignKey(Acceso, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Accesos"

 #   def nombre(self):
 #      return "{}".format(self.Nombre_de_Proyecto)
 #   
 #   def __str__(self):
 #       return self.Nombre_de_Proyecto
 #   class Meta:
 #       verbose_name_plural = "--> Proyectos"
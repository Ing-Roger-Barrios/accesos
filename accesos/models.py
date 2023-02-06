from django.db import models
import uuid
# Create your models here.




class Acceso(models.Model):
    Acceso = models.CharField(max_length=200, verbose_name='Acceso',default='')

    def __str__(self):
        return self.Acceso
    class Meta:
        verbose_name_plural = "--> Acceso"

class Seccion(models.Model):
    Nombre = models.CharField(max_length=200, verbose_name='Seccion',default='')
    accesos = models.ManyToManyField(Acceso, through='SecAcc', blank=True,)

    def __str__(self):
        return self.Nombre
    class Meta:
        verbose_name_plural = "--> Seccion"

class SecAcc(models.Model):
    Seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    Acceso = models.ForeignKey(Acceso, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "--> Secc_Acc"

class Area(models.Model):
    Area = models.CharField(max_length=200, verbose_name='Area',default='')
    Seccion = models.ManyToManyField(Seccion, through='ArSecc', blank=True,)
    
    def __str__(self):
        return self.Area
    class Meta:
        verbose_name_plural = "--> Area"

class ArSecc(models.Model):
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)
    Seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "--> ArSecc"


 #   def nombre(self):
 #      return "{}".format(self.Nombre_de_Proyecto)
 #   
 #   def __str__(self):
 #       return self.Nombre_de_Proyecto
 #   class Meta:
 #       verbose_name_plural = "--> Proyectos"
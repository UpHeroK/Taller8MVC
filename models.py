from django.db import models
class documento(models.Model):
    idoc= models.IntegerField(primary_key=True)
    nombredoc= models.CharField(max_length=32)
    descripciondoc= models.CharField(max_length=32)

class ciudad(models.Model):
    idciudad= models.IntegerField(primary_key=True)
    nombredciudad= models.CharField(max_length=32)
    descripcionciudad= models.CharField(max_length=32)

class persona(models.Model):
    idp= models.IntegerField(primary_key=True)
    nombres= models.CharField(max_length=32)
    apellidos= models.CharField(max_length=32)
    idtipdoc= models.ForeignKey(documento,on_delete=models.CASCADE)
    documentop = models.CharField(max_length=12)
    lugarderesi= models.ForeignKey(ciudad,on_delete=models.CASCADE)
    fechanac= models.DateField
    email= models.CharField(max_length=32)
    tel= models.CharField(max_length=7)
    usuario = models.CharField(max_length=10)
    password= models.CharField(max_length=10)






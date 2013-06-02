from django.db import models


class Autorizaciones(models.Model):
    #3 autorizaciones de momento
    autorizacion_medica=models.BooleanField()
    autorizacion_actividades=models.BooleanField()
    autorizacion_fotografias=models.BooleanField()
    

class Familia(models.Model):
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    nif=models.CharField(max_length=100,primary_key=True, unique=True)
    
    
class Familiares(models.Model):
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    nif=models.CharField(max_length=100,primary_key=True, unique=True)
    telefono=models.CharField(max_length=100) 
    movil=models.CharField(max_length=100) 
    email=models.CharField(max_length=100)
    rol=models.CharField(max_length=100)
    familia_id=models.ForeignKey(Familia,null=True)
     

class Socio(models.Model):
    n_asociado=models.CharField(max_length=100, primary_key=True, unique=True)
    alta=models.BooleanField()
    autorizaciones=models.ForeignKey(Autorizaciones, null=True)
    familia_id=models.ForeignKey(Familia,null=True)     
    
class D_Personales(models.Model):
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    dni=models.CharField(max_length=100)
    sexo=models.CharField(max_length=20)
    f_nacimiento=models.DateTimeField()
    direccion=models.CharField(max_length=200)
    c_postal=models.CharField(max_length=100)
    localidad=models.CharField(max_length=100)
    provincia=models.CharField(max_length=100)
    fijo=models.CharField(max_length=100)
    movil=models.CharField(max_length=100)
    f_ingreso=models.DateTimeField(blank=True, null=True)
    f_baja=models.DateTimeField(blank=True, null=True)
    seccion=models.CharField(max_length=100)
    estudios=models.TextField()
    profesion=models.TextField()
    deportes=models.TextField()
    aficiones=models.TextField()
    socio_id=models.ForeignKey(Socio)
        
class D_Medicos(models.Model):
    c_seguro=models.CharField(max_length=100)
    n_poliza=models.CharField(max_length=100)
    enfermedad=models.CharField(max_length=2, default='no')
    t_enfermedad=models.TextField()
    enfermedad_cfp=models.CharField(max_length=2, default='no')
    t_enfermedad_cfp=models.TextField()
    operado=models.CharField(max_length=2, default='no')
    t_operado=models.TextField()
    alergia=models.CharField(max_length=2, default='no')
    t_alergia=models.TextField()
    otras_alergias=models.CharField(max_length=2, default='no')
    t_otras_alergias=models.TextField()
    dieta=models.CharField(max_length=2, default='no')
    t_dieta=models.TextField()
    toma_medicamentos=models.CharField(max_length=2, default='no')
    info_adicional=models.TextField()
    socio_id=models.ForeignKey(Socio)
    
 
class D_Economicos(models.Model):
    titular=models.CharField(max_length=100)
    nif_titular=models.CharField(max_length=100)
    banco=models.CharField(max_length=100)
    sucursal=models.CharField(max_length=100)
    localidad=models.CharField(max_length=100)
    d_banco=models.CharField(max_length=100)
    d_sucursal=models.CharField(max_length=100)
    dc=models.CharField(max_length=100)
    n_cuenta=models.CharField(max_length=100)
    socio_id=models.ForeignKey(Socio)
      
class Medicamentos(models.Model):
    nombre=models.CharField(max_length=100)
    dosis=models.CharField(max_length=100)
    pauta=models.CharField(max_length=100)
    socio_id=models.ForeignKey(Socio)    
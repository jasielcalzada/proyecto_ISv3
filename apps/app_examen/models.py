from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator,MaxValueValidator
from django.utils import timezone
import datetime
# Create your models here.
class maestro(models.Model):
	user_perfil = models.OneToOneField(User, related_name="profile")
	n_empleado = models.CharField(max_length=64,primary_key=True)
	nombre = models.CharField(max_length=64)
	correo = models.EmailField()
	categoria = models.CharField(max_length=64,null = True,default="maestros")

	def __unicode__(self):
		return '%s'%(self.n_empleado)

class materia(models.Model):
	serie = models.SlugField(max_length=64, primary_key=True)#forzar al usuario a capyurarlo de una manera expresion regular
	nombre = models.CharField(max_length=64)
	maestro_a = models.ForeignKey(maestro, max_length=64)

	def __unicode__(self):
		return '%s'%(self.serie)




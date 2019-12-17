# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Paciente(id, nombreP)
# Medico(id, nombreM)
# Receta(id, medico(id)foreignKey, paciente(id)foreignKey)

class Paciente(models.Model):
	#id automatico de Django
	nombreP = models.CharField(max_length=128)

	# Funcion que guarda los datos de Paciente
	def save(self, *args, **kwargs):
		super(Paciente, self).save(*args, **kwargs)

	# Definimos el nombre en plural de la clase 
	class Meta:
		verbose_name_plural = 'Pacientes'

	def __str__(self):
		return "Paciente " + str(self.id) + " de nombre " + self.nombreP

	"""def __unicode__(self): # For Python 2, use __unicode__ too
		return self.nameP """


class Medico(models.Model):
	# id automatico
	nombreM = models.CharField(max_length=128)

	# Funcion que guarda los datos de Medico
	def save(self, *args, **kwargs):
		super(Medico, self).save(*args, **kwargs)

	# Definimos el nombre en plural de la clase
	class Meta:
		verbose_name_plural = 'Medicos'

	def __str__(self):
		return "Medico " +str(self.id) + " de nombre " + self.nombreM


class Receta(models.Model):
	# id automatico
	medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE)
	paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)

	# Funcion que guarda los datos de Receta
	def save(self, *args, **kwargs):
		super(Receta, self).save(*args, **kwargs)

	# Definimos el nombre en plural de la clase
	class Meta:
		verbose_name_plural = 'Recetas'

	def __str__(self):
		return "Receta " +str(self.id) + " de medico " + self.medico_id.nombreM + " y paciente " + self.paciente_id.nombreP

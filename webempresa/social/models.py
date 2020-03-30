from django.db import models

# Create your models here.
class Link(models.Model):
	key = models.SlugField(verbose_name='Nombre clave', unique=True, max_length=100)
	name = models.CharField(verbose_name='Red social', max_length=200)
	url = models.URLField(verbose_name='Enlace', null=True, blank=True, max_length=200)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'enlace'

	def __str__(self):
		return self.name
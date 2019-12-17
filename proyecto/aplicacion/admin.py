from django.contrib import admin
from aplicacion.models import Medico, Paciente, Receta

#class MedicoAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}

#class PacienteAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}

class RecetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'medico', 'paciente')

# Register your models here.
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Receta)
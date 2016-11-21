from django.contrib import admin
from .models import maestro, materia
# Register your models here.
@admin.register(maestro)
class maestro_admin(admin.ModelAdmin):
	list_display = ('n_empleado','user_perfil','nombre','correo','categoria')

@admin.register(materia)
class materia_admin(admin.ModelAdmin):
	list_display = ('serie','nombre','maestro_a')
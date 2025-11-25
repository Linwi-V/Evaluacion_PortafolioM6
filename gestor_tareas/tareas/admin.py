from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'completada', 'fecha_creacion')
    list_filter = ('completada', 'fecha_creacion', 'usuario')
    search_fields = ('titulo', 'descripcion')
    list_editable = ('completada',)
    date_hierarchy = 'fecha_creacion'
    
    fieldsets = (
        ('Información básica', {
            'fields': ('usuario', 'titulo', 'descripcion')
        }),
        ('Estado', {
            'fields': ('completada',)
        }),
    )
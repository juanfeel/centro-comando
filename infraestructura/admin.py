from django.contrib import admin
from .models import NodoServidor, RegistroAuditoria, IncidenciaServidor  # <--- agrega IncidenciaServidor aquí

# Acciones masivas personalizadas
@admin.action(description="Activar Producción Masiva")
def marcar_como_produccion(modeladmin, request, queryset):
    queryset.update(en_produccion=True)


@admin.action(description="Poner en Mantenimiento")
def marcar_como_mantenimiento(modeladmin, request, queryset):
    queryset.update(en_produccion=False)


@admin.action(description="Marcar como Resueltas")
def marcar_como_resueltas(modeladmin, request, queryset):
    queryset.update(resuelta=True)


@admin.register(NodoServidor)
class NodoServidorAdmin(admin.ModelAdmin):

    # Columnas que se mostrarán en la tabla principal
    list_display = (
        'nombre_host',
        'direccion_ip',
        'motor_contenedores',
        'proxy_inverso',
        'en_produccion'
    )

    # Filtros laterales para hacer búsquedas rápidas
    list_filter = (
        'motor_contenedores',
        'proxy_inverso',
        'en_produccion'
    )

    # Barra de búsqueda superior
    search_fields = (
        'nombre_host',
        'direccion_ip'
    )

    # Orden por defecto
    ordering = ('-fecha_despliegue',)

    # Acciones masivas registradas en el panel
    actions = [marcar_como_produccion, marcar_como_mantenimiento]



@admin.register(RegistroAuditoria)
class RegistroAuditoriaAdmin(admin.ModelAdmin):
    list_display = ('servidor', 'detalles', 'fecha_evento')
    list_filter = ('fecha_evento', 'servidor')
    search_fields = ('servidor__nombre_host', 'detalles')
    readonly_fields = ('fecha_evento',)


@admin.register(IncidenciaServidor)
class IncidenciaServidorAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'servidor', 'severidad', 'resuelta', 'fecha_registro')
    list_filter = ('severidad', 'resuelta', 'servidor')
    search_fields = ('titulo', 'descripcion', 'servidor__nombre_host')
    ordering = ('-fecha_registro',)
    actions = [marcar_como_resueltas]
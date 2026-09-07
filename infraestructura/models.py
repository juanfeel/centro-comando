from django.db import models
from django.core.exceptions import ValidationError

def validar_ip_corporativa(value):
    if value.startswith("192.168.100."):
        raise ValidationError("Las direcciones IP en el segmento 192.168.100.x están reservadas para pruebas internas de aislamiento.")

class NodoServidor(models.Model):
    # Opciones predefinidas para el panel
    MOTORES_CONTENEDOR = [
        ('docker', 'Docker'),
        ('podman', 'Podman'),
        ('lxc', 'LXC Linux Containers'),
        ('ninguno', 'Sin contenedores'),
    ]

    nombre_host = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Hostname"
    )

    direccion_ip = models.GenericIPAddressField(
        verbose_name="Dirección IP",
        validators=[validar_ip_corporativa]
    )

    motor_contenedores = models.CharField(
        max_length=20,
        choices=MOTORES_CONTENEDOR,
        default='podman',
        verbose_name="Motor de Contenedores"
    )

    proxy_inverso = models.BooleanField(
        default=True,
        verbose_name="¿Enrutado por Nginx?"
    )

    en_produccion = models.BooleanField(
        default=True,
        verbose_name="Estado Producción"
    )

    fecha_despliegue = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.nombre_host} [{self.direccion_ip}]"

    class Meta:
        verbose_name = "Nodo de Servidor"
        verbose_name_plural = "Flota de Servidores"

class RegistroAuditoria(models.Model):
    # Campo de Relación: Llave foránea hacia NodoServidor
    servidor = models.ForeignKey(
        NodoServidor,
        on_delete=models.PROTECT,
        related_name='auditorias'
    )

    # Descripción del Evento
    detalles = models.TextField(
        verbose_name="Detalle del Evento"
    )

    # Marca de Tiempo: Registra la fecha y hora actual automáticamente
    fecha_evento = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Auditoría de {self.servidor.nombre_host} - {self.fecha_evento.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Registro de Auditoría"
        verbose_name_plural = "Historial de Auditorías"

class IncidenciaServidor(models.Model):
    SEVERIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('critica', 'Crítica'),
    ]

    servidor = models.ForeignKey(
        NodoServidor,
        on_delete=models.CASCADE,
        related_name='incidencias'
    )

    titulo = models.CharField(
        max_length=150,
        verbose_name="Título de la Incidencia"
    )

    descripcion = models.TextField(
        verbose_name="Descripción del Fallo"
    )

    severidad = models.CharField(
        max_length=10,
        choices=SEVERIDAD_CHOICES,
        default='media'
    )

    resuelta = models.BooleanField(
        default=False,
        verbose_name="¿Incidencia Resuelta?"
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"[{self.severidad.upper()}] {self.titulo} - {self.servidor.nombre_host}"

    class Meta:
        verbose_name = "Incidencia de Servidor"
        verbose_name_plural = "Incidencias de Servidores"
        ordering = ['-fecha_registro']
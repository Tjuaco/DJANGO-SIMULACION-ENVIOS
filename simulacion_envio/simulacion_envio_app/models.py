from django.db import models

# DEFINE MODELO SIMULACION
class Simulacion(models.Model): 
    nombre_empleado = models.CharField(max_length=30)
    cantidad_unidades = models.PositiveIntegerField()
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_articulo = models.CharField(max_length=100)
    codigo_articulo = models.IntegerField()
    nombre_proveedor = models.CharField(max_length=100)
   
    #CAMPOS PARA RESULTADOS CALCULADOS (VALORES NULOS Y EN BLANCO)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tasa_aduana = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    iva = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    impuesto_aduana = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


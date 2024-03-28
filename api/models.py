from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    id_fb = models.CharField(max_length=20, unique=True )
    sku = models.CharField(max_length=20)
    planta_primaria = models.CharField(max_length=10)
    nombre_producto = models.CharField(max_length=50)
    nombre_abreviado = models.CharField(max_length=20)
    ean = models.CharField(max_length=15)
    destino_primaria = models.CharField(max_length=10, default='EC')
    version_primaria = models.CharField(max_length=10)
    nb_primaria = models.CharField(max_length=5)
    dias_caducidad = models.IntegerField()
    id_path = models.CharField(max_length=30)
    familia_path = models.CharField(max_length=30)
    familia_path_colos = models.CharField(max_length=100)
    descripcion_linea_1 = models.TextField(blank=True, null=True)
    descripcion_linea_2 = models.TextField(blank=True, null=True)
    descripcion_linea_3 = models.TextField(blank=True, null=True)
    proteina = models.FloatField()
    humedad = models.FloatField()
    ceniza = models.FloatField()
    grasa = models.FloatField()
    fibra = models.FloatField()
    ingredientes_linea_1 = models.TextField(blank=True, null=True)
    ingredientes_linea_2 = models.TextField(blank=True, null=True)
    ingredientes_linea_3 = models.TextField(blank=True, null=True)
    ingredientes_linea_4 = models.TextField(blank=True, null=True)
    ingredientes_linea_5 = models.TextField(blank=True, null=True)
    registro_sanitario = models.CharField(max_length=20)
    fabricado_para = models.CharField(max_length=100)
    direccion_fabricante = models.CharField(max_length=100)
    ruc_fabricante = models.CharField(max_length=100)
    version_secundaria = models.CharField(max_length=5, blank=True, null=True)
    cantidad_terciaria = models.CharField(max_length=10, blank=True, null=True)
    peso_neto_terciaria = models.CharField(max_length=10, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    is_actualizado = models.BooleanField()
    is_new = models.BooleanField()
    id_ubicacion = models.IntegerField()
    nombre_ubicacion = models.CharField(max_length=10)
    estado = models.CharField(max_length=10)

class OrdenProduccion(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=20)
    planta_primaria = models.CharField(max_length=10)
    nombre_producto = models.CharField(max_length=100)
    nombre_abreviado = models.CharField(max_length=20)
    ean = models.CharField(max_length=15)
    destino_primaria = models.CharField(max_length=10, default='EC')
    version_primaria = models.CharField(max_length=10)
    nb_primaria = models.CharField(max_length=5)
    dias_caducidad = models.IntegerField()
    id_path = models.CharField(max_length=30)
    familia_path = models.CharField(max_length=30)
    familia_path_colos = models.CharField(max_length=100)
    descripcion_linea_1 = models.TextField(blank=True, null=True)
    descripcion_linea_2 = models.TextField(blank=True, null=True)
    descripcion_linea_3 = models.TextField(blank=True, null=True)
    proteina = models.FloatField()
    humedad = models.FloatField()
    ceniza = models.FloatField()
    grasa = models.FloatField()
    fibra = models.FloatField()
    ingredientes_linea_1 = models.TextField(blank=True, null=True)
    ingredientes_linea_2 = models.TextField(blank=True, null=True)
    ingredientes_linea_3 = models.TextField(blank=True, null=True)
    ingredientes_linea_4 = models.TextField(blank=True, null=True)
    ingredientes_linea_5 = models.TextField(blank=True, null=True)
    registro_sanitario = models.CharField(max_length=20)
    fabricado_para = models.CharField(max_length=100)
    direccion_fabricante = models.CharField(max_length=100)
    ruc_fabricante = models.CharField(max_length=100)
    version_secundaria = models.CharField(max_length=5, blank=True, null=True)
    cantidad_terciaria = models.CharField(max_length=10, blank=True, null=True)
    peso_neto_terciaria = models.CharField(max_length=10, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    estado = models.CharField(max_length=10)

    # Campos específicos de OrdenProduccion
    fecha_final = models.DateTimeField()
    planta = models.IntegerField()
    prensa = models.CharField(max_length=5, blank=True, null=True)
    prensa_numero = models.IntegerField(blank=True, null=True)  # prensa_numero
    linea = models.CharField(max_length=5)
    lote_completo = models.CharField(max_length=20, blank=True, null=True)
    lote_numeros = models.IntegerField()
    turno = models.IntegerField()
    inicio_contador_general = models.IntegerField(blank=True, null=True)
    sscc_inicio = models.CharField(max_length=30, blank=True, null=True)
    inicio_contador = models.IntegerField(blank=True, null=True)
    id_producto = models.IntegerField(blank=True, null=True)
    id_fb_producto = models.CharField(max_length=20, null=True )
    fin_contador_general = models.IntegerField(blank=True, null=True)
    fin_contador = models.IntegerField(blank=True, null=True)
    fecha_caducidad_string = models.CharField(max_length=10, blank=True, null=True)


class Palet(models.Model):
    id = models.AutoField(primary_key=True)
    id_fb = models.CharField(max_length=50)
    sku = models.CharField(max_length=25)
    nombre_producto = models.CharField(max_length=100)
    ean13 = models.CharField(max_length=100)
    planta_primaria = models.CharField(max_length=10)
    linea = models.CharField(max_length=5)
    llenadora = models.CharField(max_length=5)
    prensa = models.CharField(max_length=5)
    prensa_numero = models.IntegerField()
    version_primaria = models.IntegerField()
    lote_completo = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    sscc = models.CharField(max_length=25, unique=True)
    fecha_elaboracion = models.DateField()
    fecha_caducidad = models.DateField()
    numero_palet = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    id_bodega_origen = models.IntegerField()
    id_bodega_destino = models.IntegerField()
    movimientos_id = ArrayField(models.IntegerField(), blank=True, default=list)
    movimientos_nombre = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    fechas_movimientos = ArrayField(models.DateField(), blank=True, default=list)
    usuarios_movimientos = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    turno = models.IntegerField()
    id_usuario = models.CharField(max_length=50)
    id_orden_produccion = models.IntegerField()
    subido_a_firebase = models.BooleanField()
    subido_a_vitacontrol = models.BooleanField()
    fecha_caducidad_string = models.CharField(max_length=10, blank=True, null=True)

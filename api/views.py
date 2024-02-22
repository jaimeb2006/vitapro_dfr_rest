
# Create your views here.

from drf_spectacular.utils import extend_schema , extend_schema_view
from rest_framework import viewsets, filters

# from api.serializers import TaskSerializer, ProductoSerializer
from api.serializers import  OrdenProduccionSerializer, ProductoSerializer
from api.models import  OrdenProduccion, Producto
@extend_schema_view(
    list= extend_schema(description= 'Pernite obtener una lista de Productos.'),
    retrieve=extend_schema(description= 'Permite obtener una Producto.'),
    create=extend_schema (description='Permite crear una Producto.'),
    update=extend_schema (description='Pernite actualizar una Producto.'),
    destroy=extend_schema(description ='Pernite eliminar una Producto.'),
)
# class TaskViewSet(viewsets.ModelViewSet):
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()

class ProductoViewSet(viewsets.ModelViewSet):
    search_fields = ['nombre_producto', 'sku', 'id_fb', 'ean']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

class OrdenProduccionViewSet(viewsets.ModelViewSet):
    search_fields = ['id','lote_completo','lote_numeros','turno','nombre_producto', 'sku', 'ean']
    filter_backends = (filters.SearchFilter,)
    serializer_class = OrdenProduccionSerializer
    queryset = OrdenProduccion.objects.all()

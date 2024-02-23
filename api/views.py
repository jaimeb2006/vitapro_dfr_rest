
# Create your views here.

from django.http import JsonResponse
from datetime import datetime
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

class ProductoViewSet(viewsets.ModelViewSet):
    search_fields = ['nombre_producto', 'sku', 'id_fb', 'ean']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

@extend_schema_view(
    list=extend_schema(description='Permite obtener una lista de Ordenes de Producción.'),
    retrieve=extend_schema(description='Permite obtener una Orden de Producción específica.'),
    create=extend_schema(description='Permite crear una Orden de Producción.'),
    update=extend_schema(description='Permite actualizar una Orden de Producción.'),
    destroy=extend_schema(description='Permite eliminar una Orden de Producción.'),
)
class OrdenProduccionViewSet(viewsets.ModelViewSet):
    search_fields = ['id','lote_completo','lote_numeros','turno','nombre_producto', 'sku', 'ean']
    filter_backends = (filters.SearchFilter,)
    serializer_class = OrdenProduccionSerializer
    queryset = OrdenProduccion.objects.all()


def current_date(request):
    now = datetime.now()
    return JsonResponse({'current_date': now})

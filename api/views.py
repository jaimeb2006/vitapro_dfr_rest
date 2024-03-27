
# Create your views here.

from django.http import JsonResponse
from datetime import datetime
from drf_spectacular.utils import extend_schema , extend_schema_view
from rest_framework import viewsets, filters

# from api.serializers import TaskSerializer, ProductoSerializer
from api.serializers import  OrdenProduccionSerializer, PaletSerializer, ProductoSerializer
from api.models import  OrdenProduccion, Palet, Producto

from django_filters.rest_framework import DjangoFilterBackend
import django_filters
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


class OrdenProduccionFilter(django_filters.FilterSet):
    class Meta:
        model = OrdenProduccion
        fields = {
            'turno': ['exact', 'icontains'],
            'lote_completo': ['exact', 'icontains'],
            'id_producto': ['exact', 'icontains'],
            'linea': ['exact', 'icontains'],
            # Puedes añadir más campos y tipos de filtro aquí
        }

@extend_schema_view(
    list=extend_schema(description='Permite obtener una lista de Ordenes de Producción.'),
    retrieve=extend_schema(description='Permite obtener una Orden de Producción específica.'),
    create=extend_schema(description='Permite crear una Orden de Producción.'),
    update=extend_schema(description='Permite actualizar una Orden de Producción.'),
    destroy=extend_schema(description='Permite eliminar una Orden de Producción.'),
)
class OrdenProduccionViewSet(viewsets.ModelViewSet):
    # search_fields = ['id','lote_completo','lote_numeros','turno','nombre_producto', 'sku', 'ean','turno']
    queryset = OrdenProduccion.objects.all()
    serializer_class = OrdenProduccionSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_class = OrdenProduccionFilter
    ordering_fields = ['id']
    ordering = ['-id'] 



class PaletFilter(django_filters.FilterSet):
    class Meta:
        model = Palet
        fields = {
            'lote_completo': ['exact', 'icontains'],
            'subido_a_firebase': ['exact', 'icontains'],
            'subido_a_vitacontrol': ['exact', 'icontains'],
            'id': ['exact', 'icontains'],
            # Puedes añadir más campos y tipos de filtro aquí
        }

@extend_schema_view(
    list=extend_schema(description='Permite obtener una lista de Palets'),
    retrieve=extend_schema(description='Permite obtener una Orden de Palet específica.'),
    create=extend_schema(description='Permite crear una Palet.'),
    update=extend_schema(description='Permite actualizar una Palet.'),
    destroy=extend_schema(description='Permite eliminar una Palet.'),
)
class PaletViewSet(viewsets.ModelViewSet):
    # search_fields = ['id','lote_completo','lote_numeros','turno','nombre_producto', 'sku', 'ean','turno']
    queryset = Palet.objects.all()
    serializer_class = PaletSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_class = PaletFilter
    ordering_fields = ['id']
    ordering = ['-id'] 


def current_date(request):
    now = datetime.now()
    return JsonResponse({'current_date': now})

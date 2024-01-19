from django.shortcuts import render

# Create your views here.

from drf_spectacular.utils import extend_schema , extend_schema_view
from rest_framework import viewsets

# from api.serializers import TaskSerializer, ProductoSerializer
from api.serializers import  ProductoSerializer
from api.models import  Producto
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
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView 
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from api import views

from api.views import OrdenProduccionViewSet, ProductoViewSet
router:ExtendedSimpleRouter= ExtendedSimpleRouter()
# router.register(r"tasks", TaskViewSet)
router.register(r"productos", ProductoViewSet)
router.register(r"ordenproduccion", OrdenProduccionViewSet)

urlpatterns = [
    path('schema/',SpectacularAPIView. as_view(), name= 'schema'),
    path ('schema/swagger/',SpectacularSwaggerView.as_view(url_name= 'api:schema'), name=  'swagger'),
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name= 'token_refresh'),
    path('token/verify/',TokenVerifyView.as_view(), name='token_refresh'),
    path('current-date/', views.current_date, name='current-date'),
    path('',include (router.urls)),
]
from django.urls import path
from django.views.generic import TemplateView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PointImageViewSet, PointViewSet, WriterViewSet, RouteViewSet




# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'point-image',PointImageViewSet,basename="point-image")
router.register(r'point',PointViewSet,basename="point")
router.register(r'writer',WriterViewSet,basename="writer")
router.register(r'route',RouteViewSet,basename="route")


app_name = 'amrl'

urlpatterns = [
    #path('', TemplateView.as_view(template_name="amrl/index.html")),
    path('api/', include(router.urls)),
]
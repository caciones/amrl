from rest_framework import viewsets
from .models import PointImage
from .serializers import PointImageSerializer
from .models import Point
from .serializers import PointSerializer
from .models import Writer
from .serializers import WriterSerializer
from .models import Route
from .serializers import RouteSerializer



class PointImageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = PointImage.objects.all()
    serializer_class = PointImageSerializer


class PointViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class WriterViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer


class RouteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

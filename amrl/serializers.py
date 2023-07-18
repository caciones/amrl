import json
from rest_framework import serializers
from .models import PointImage, Point, Writer, Route
from .route_service import RouteService


class PointImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True, allow_empty_file=False)

    class Meta:
        model = PointImage
        fields = ['id', 'name', 'caption', 'image', 'point']

class WriterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required = True)

    class Meta:
        model = Writer
        fields = ['id', 'name', 'birth_date', 'nationality']

class PointSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required = True)
    location = serializers.SerializerMethodField()
    images = PointImageSerializer(many=True, source="pointimage_set",)

    class Meta:
        model = Point
        fields = ['id', 'title', 'text', 'sequence_number', 'location', 'speech_file', 'route', 'images']

    def get_location(self, obj):
        return {'lat': obj.location[1], 'lng': obj.location[0],}


class RouteSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required = True)
    points = PointSerializer(read_only=True, many=True, source='point_set')
    writer = WriterSerializer(read_only=True, many=True)
    directions = serializers.SerializerMethodField(read_only=True)
    distance = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Route
        fields = ['id', 'name', 'city', 'writer', 'points', "directions", "distance"]

    def get_directions(self, obj):
        route_service = RouteService(obj)
        return route_service.directions()

    def get_distance(self, obj):
        route_service = RouteService(obj)
        return route_service.distance()

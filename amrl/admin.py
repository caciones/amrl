from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Route, Writer, Point, PointImage

@admin.register(Point)
class PointAdmin(OSMGeoAdmin):
    list_display = ('title', 'sequence_number', 'route',)


class PointImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'point', 'route')

    def route(self, obj):
        try:
            return obj.point.route.name
        except Exception:
            return "n/a"


class RouteAdmin(admin.ModelAdmin):
    filter_horizontal = ['writer']

admin.site.register(PointImage, PointImageAdmin)
admin.site.register(Writer)
admin.site.register(Route, RouteAdmin)

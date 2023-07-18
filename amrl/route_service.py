import googlemaps
from django.conf import settings


class RouteService:
    def __init__(self, route):
        self.route = route

    def km(self, data):
        tmp = []
        for item in data["rows"]:
            for elem in item["elements"]:
                tmp.append(elem["distance"])
        r = max(tmp, key=lambda x:x["value"])
        return r["text"]

    def hours(self, data):
        tmp = []
        for item in data["rows"]:
            for elem in item["elements"]:
                tmp.append(elem["duration"])
        r = max(tmp, key=lambda x:x["value"])
        return r["text"]

    def geopoint(self, point):
        return {'lat': point.location[1], 'lng': point.location[0],}

    def directions(self):
        origin = {}
        destination = {}
        waypoints = []

        point_origin = self.route.point_set.first()
        if point_origin:
            origin = self.geopoint(point_origin)

        point_destination = self.route.point_set.last()
        if point_destination:
            destination = self.geopoint(point_destination)

        for point in self.route.point_set.exclude(id=point_origin.id).exclude(id=point_destination.id).order_by('sequence_number'):
            waypoints.append({'location': self.geopoint(point)})

        return {
            "origin": origin,
            "destination": destination,
            "waypoints": waypoints,
            "travelMode": "WALKING"
        }
    
    def distance(self):
        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_KEY)

        origins = []
        destinations = []

        qs = self.route.point_set.order_by('sequence_number')
        for current, next in zip(qs, qs[1:]):
            origins.append(self.geopoint(current))
            destinations.append(self.geopoint(next))

        data = {
            "origins": origins,
            "destinations": destinations,
            "mode": "walking",
            "units": "metric",
        }
        res = gmaps.distance_matrix(**data)

        return {
            "km": self.km(res),
            "estimated_duration": self.hours(res)
        }
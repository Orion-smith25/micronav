from .waypoint import haversine

class Geofence:
    def __init__(self, center_lat, center_lon, radius):
        self.center_lat = center_lat
        self.center_lon = center_lon
        self.radius = radius

    def is_inside(self, lat, lon):
        distance = haversine(self.center_lat, self.center_lon, lat, lon)
        return distance <= self.radius

    def distance_to_boundary(self, lat, lon):
        distance = haversine(self.center_lat, self.center_lon, lat, lon)
        return self.radius - distance

import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def bearing(lat1, lon1, lat2, lon2):
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dlambda = math.radians(lon2 - lon1)
    y = math.sin(dlambda) * math.cos(phi2)
    x = math.cos(phi1)*math.sin(phi2) - math.sin(phi1)*math.cos(phi2)*math.cos(dlambda)
    return (math.degrees(math.atan2(y, x)) + 360) % 360

class WaypointNavigator:
    def __init__(self, waypoints=None):
        self.waypoints = waypoints or []
        self.current_index = 0

    def add_waypoint(self, lat, lon):
        self.waypoints.append({"lat": lat, "lon": lon})

    def next_waypoint(self):
        if self.current_index < len(self.waypoints):
            wp = self.waypoints[self.current_index]
            self.current_index += 1
            return wp
        return None

    def current_waypoint(self):
        if self.current_index < len(self.waypoints):
            return self.waypoints[self.current_index]
        return None

    def distance_to(self, current_lat, current_lon):
        wp = self.current_waypoint()
        if wp is None:
            return 0.0
        return haversine(current_lat, current_lon, wp["lat"], wp["lon"])

    def bearing_to(self, current_lat, current_lon):
        wp = self.current_waypoint()
        if wp is None:
            return 0.0
        return bearing(current_lat, current_lon, wp["lat"], wp["lon"])

    def is_complete(self):
        return self.current_index >= len(self.waypoints)

    def reset(self):
        self.current_index = 0

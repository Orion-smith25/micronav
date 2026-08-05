"""waynav - Lightweight autonomous navigation library"""

from .waypoint import WaypointNavigator, haversine, bearing
from .pid import PIDController
from .geofence import Geofence

__version__ = "0.1.1"
__author__ = "Smith (Maritime Autonomy Lab)"
__all__ = ["WaypointNavigator", "haversine", "bearing", "PIDController", "Geofence"]

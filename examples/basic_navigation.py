#!/usr/bin/env python3
"""Basic waypoint navigation demo"""

from micronav import WaypointNavigator, PIDController, Geofence

waypoints = [
    {"lat": -6.175, "lon": 106.827},
    {"lat": -6.125, "lon": 106.655},
    {"lat": -6.100, "lon": 106.700},
    {"lat": -6.175, "lon": 106.827}
]

nav = WaypointNavigator(waypoints)
print(f"Mission: {len(waypoints)} waypoints")

gps = {"lat": -6.175, "lon": 106.827, "heading": 0.0}
pid = PIDController(kp=1.0, ki=0.1, kd=0.05, setpoint=0.0, output_limits=(-30, 30))
fence = Geofence(center_lat=-6.175, center_lon=106.827, radius=500)

print("\n--- Starting Navigation ---")
while not nav.is_complete():
    distance = nav.distance_to(gps["lat"], gps["lon"])
    bearing = nav.bearing_to(gps["lat"], gps["lon"])
    correction = pid.update(bearing, dt=0.1)
    gps["heading"] += correction

    print(f"WP {nav.current_index+1}/{len(waypoints)} | "
          f"Dist: {distance:.1f}m | "
          f"Bearing: {bearing:.1f}deg | "
          f"Correction: {correction:+.1f}deg")

    if not fence.is_inside(gps["lat"], gps["lon"]):
        print("Outside geofence!")
        break

    if distance < 10.0:
        print(f"Waypoint {nav.current_index+1} reached!")
        nav.next_waypoint()

print("--- Mission Complete ---")

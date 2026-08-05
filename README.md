# waynav

**Lightweight autonomous navigation library — anywhere Python runs.**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows%20%7C%20Termux%20%7C%20Docker-orange.svg)]()

---

## Overview

`waynav` is a minimalist Python library for autonomous navigation tasks:

- **Waypoint navigation** with Haversine distance and bearing
- **PID controller** for heading and speed
- **Geofencing** — virtual boundary enforcement
- **Zero dependencies** — only Python standard library
- **Runs anywhere** — laptop, Raspberry Pi, Docker, Android/Termux

---

## Installation

```bash
pip install waynav

Or from source:

```bash
git clone https://github.com/Orion-smith25/micronav.git
cd waynav
pip install -e .
```

---

Quick Start

```python
from waynav import WaypointNavigator, PIDController, Geofence

waypoints = [
    {"lat": -6.175, "lon": 106.827},
    {"lat": -6.125, "lon": 106.655},
]

nav = WaypointNavigator(waypoints)
current = {"lat": -6.175, "lon": 106.827}

print(f"Distance: {nav.distance_to(current):.1f}m")
print(f"Bearing: {nav.bearing_to(current):.1f}deg")

pid = PIDController(kp=1.0, ki=0.1, kd=0.05)
correction = pid.update(target=90.0, current=45.0)
print(f"PID correction: {correction:.1f}")

fence = Geofence(center_lat=-6.175, center_lon=106.827, radius=500)
print(f"Inside geofence: {fence.is_inside(current)}")
```

---

Docker

```bash
docker build -t waynav .
docker run -it waynav python3 examples/basic_navigation.py
```

---

Modules

Module Description
waypoint Waypoint management, Haversine distance, bearing
pid PID controller for heading and speed
geofence Circular geofence boundary enforcement
utils Coordinate conversion, angle normalization

---

Platform Support

Platform Status
Linux (x86_64) Full
macOS Full
Windows Full
Raspberry Pi Full
Termux (Android) Full
Docker Full

---

Related Projects

· open-nav-core
· maritime-vessel-design

---

License

MIT License — see LICENSE

---

Maintained by the Maritime Autonomy Lab.

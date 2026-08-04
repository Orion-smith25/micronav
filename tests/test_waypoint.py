from micronav.waypoint import haversine, bearing, WaypointNavigator

def test_haversine():
    dist = haversine(0, 0, 0, 0)
    assert dist == 0.0
    dist = haversine(51.5074, -0.1278, 48.8566, 2.3522)
    assert 340000 < dist < 350000

def test_bearing():
    brg = bearing(0, 0, 90, 0)
    assert 0 <= brg <= 360

def test_waypoint_navigator():
    nav = WaypointNavigator([{"lat": 0, "lon": 0}, {"lat": 1, "lon": 1}])
    assert not nav.is_complete()
    assert nav.next_waypoint() == {"lat": 0, "lon": 0}
    assert nav.next_waypoint() == {"lat": 1, "lon": 1}
    assert nav.is_complete()

if __name__ == "__main__":
    test_haversine()
    test_bearing()
    test_waypoint_navigator()
    print("All tests passed!")

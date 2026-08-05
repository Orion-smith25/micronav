import math

def normalize_angle(angle):
    return angle % 360

def angle_difference(target, current):
    return (target - current + 180) % 360 - 180

def knots_to_ms(knots):
    return knots * 0.514444

def ms_to_knots(ms):
    return ms / 0.514444

def decimal_to_dms(decimal):
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = (decimal - degrees - minutes/60) * 3600
    return degrees, minutes, seconds

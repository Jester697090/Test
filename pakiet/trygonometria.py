import math

def rad2deg(radAngle):
    return 180 * radAngle / math.pi

def deg2rad(degAngle):
    return math.pi * degAngle / 180

def sine(degAngle):
    return math.sin(deg2rad(degAngle))

def cosine(degAngle):
    return math.cos(deg2rad(degAngle))

def tangent(degAngle):
    if degAngle % 180 == 90:
        return
    return math.tan(deg2rad(degAngle))

def cotangent(degAngle):
    if degAngle % 180 == 0:
        return
    return 1 / math.tan(deg2rad(degAngle))

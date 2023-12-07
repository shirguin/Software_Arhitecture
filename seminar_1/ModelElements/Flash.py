from Point3D import Point3D
from Angle3d import Angle3D
from Color import Color


class Flash:
    location = Point3D
    angle = Angle3D
    color = Color
    power = float

    def __init__(self, color, angle, location, power):
        self.color = color
        self.power = power
        self.angle = angle
        self.location = location

    def Move(self, Point3D):
        return Point3D

    def Rotate(self, Angle3d):
        return Angle3d
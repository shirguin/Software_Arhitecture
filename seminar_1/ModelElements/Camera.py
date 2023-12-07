from Point3D import Point3D
from Angle3d import Angle3D


class Camera:
    location = Point3D
    angle = Angle3D

    def __init__(self, location, angle):
        self.location = location
        self.angle = angle

    def rotate(self, location):
        pass

    def movie(self, angle):
        pass
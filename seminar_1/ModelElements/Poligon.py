from Point3D import Point3D


class Poligon (Point3D):
    points = Point3D

    def __init__(self, points):
        self.points = list(points)

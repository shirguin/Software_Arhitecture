from Triangle import Triangle
from Square import Square
from Sphere import Sphere
from Software_architecture.sem3.ISP.Cube import Cube


def main():
    triangle = Triangle().find_area()
    square = Square().find_area()
    sphere = Sphere().find_area()
    cube = Cube().find_volume()
    # lst = [cube, sphere, square, triangle]
    # for i in lst:
    #    print(i)
    print(triangle, square, sphere, cube)

main()

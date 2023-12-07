from Software_architecture.sem3.ISP.Rectangle import Rectangle


class Triangle(Rectangle):
    def find_area(self):
        print ("найдена прощадь треугольника")


if __name__ == '__main__':
    triangle = Triangle()
    triangle.find_area()
from Software_architecture.sem3.ISP.Rectangle import Rectangle


class Square(Rectangle):
    def find_area(self):
        print ('найдена прощадь квадрата')

    def find_perimeter(self):
        print ('найден периметр квадрата')
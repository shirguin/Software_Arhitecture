from PoligonalModel import PoligonalModel
from Flash import Flash
from Camera import Camera


class Scene:
    id: int
    list.models = PoligonalModel
    list.flashes = Flash
    list.cameras = Camera

    def __init__(self, id, models, flashes, cameras):
        self.id = id
        # try:
        #     if len(models) == 0 or None:
        # except IndexError:
        #     print("Список пуст")
        self.models = models

        self.flashes = flashes
        self.cameras = cameras

    def Metod1(self, type1):
        return type(type1)

    def Metod2(self, type2):
        return type(type2)
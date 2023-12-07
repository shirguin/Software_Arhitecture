from Texture import Texture
from Poligon import Poligon


class PoligonalModel:
    list.textures = Texture
    list.poligons = Poligon

    def __init__(self, textures, poligons):
        self.textures = list(textures)
        self.poligons = list(poligons)
        poligons.append(Poligon)


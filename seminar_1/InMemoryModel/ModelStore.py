from numpy import size

from IModelChanger import IModelChanger
from IModelChangedObserver import IModelChangedObserver
from ModelElements.Camera import Camera
from ModelElements.Scene import Scene
from ModelElements.Flash import Flash
from ModelElements.PoligonalModel import PoligonalModel


class ModelStore (IModelChanger):
    sender = IModelChanger
    list.models = PoligonalModel
    list.scenes = Scene
    list.flashes = Flash
    list.cameras = Camera
    __change_observes = IModelChangedObserver
    __n = int

    def __init__(self, models, scenes, flashes, cameras, __changes_observes, __n):
        self.models = __changes_observes
        self.models = models
        self.scenes = scenes
        self.models = flashes
        self.models = cameras

    def Getscene(self, sceneId: int):
        return self.scenes.get(sceneId)

    def NotifyChanger(self, sender):
        pass


    
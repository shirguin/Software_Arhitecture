from abc import ABCMeta


class IModelChangedObserver(metaclass=ABCMeta):
    def apply_update_model(self):
        return None
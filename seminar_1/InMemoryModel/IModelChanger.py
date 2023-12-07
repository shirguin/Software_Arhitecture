from abc import ABCMeta


class IModelChanger(metaclass=ABCMeta):
    def notify_change(self, sender):
        return sender
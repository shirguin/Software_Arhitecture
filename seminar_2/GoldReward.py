from IGameItem import IGameItem


class GoldReward(IGameItem):
    def open(self):
        print('Gold')
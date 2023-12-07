from ItemFabric import ItemFabric
from StoneReward import StoneReward


class StoneGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return StoneReward()

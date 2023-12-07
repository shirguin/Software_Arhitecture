from ItemFabric import ItemFabric
from GoldReward import GoldReward


class GoldGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GoldReward()
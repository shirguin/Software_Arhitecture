from Data.Carrier import Carrier


class CarrierRepository:
    def __init__(self, carriers: Carrier):
        self.__carriers = carriers

    def carrier_repository(self):
        self.__carriers = []

    def set_carrier(self, carrier):
        self.__carriers.add(carrier)

    def get_carrier(self, index):
        return self.__carriers.get(index)

    def delete_carrier(self, index):
        self.__carriers.remove(index)

    def get_carriers(self):
        return self.__carriers
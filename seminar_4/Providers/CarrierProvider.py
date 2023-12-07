from Data.BankAccount import BankAccount
from Data.Carrier import Carrier
from Data.Repositories import CarrierRepository


class CarrierProvider:
    carrier_repository = CarrierRepository

    def __init__(self, carrier_repository):
        self.__carrier_repository = carrier_repository

    def create_carrier(self, routes: list, account: BankAccount):
        carrier = Carrier(self.carrier_repository.get_carriers().size() + 1, routes, account)
        self.carrier_repository.setCarrier(carrier)

    def update_carrier(self, index, route):
        self.carrier_repository.get_carrier(index).add_route(route)

    def delete_carrier(self, index):
        self.carrier_repository.delete_carrier(index)

    def read_carrier(self, index):
        return self.carrier_repository.get_carrier(index)


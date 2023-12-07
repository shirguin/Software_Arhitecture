from BankAccount import BankAccount


class Carrier:

    def __init__(self, id: int, routes: [], account: BankAccount):
        self.__id = id
        self.__routes = routes
        self.__account = account

    def set_id(self, id):
        if type(id) in (int, float):
            self.__id = id
        else:
            raise ValueError("данные должны быть числами")

    def get_id(self):
        return self.__id

    def set_account(self):
        self.__account = BankAccount

    def get_account(self):
        return self.__account

    def add_route(self, route: str):
        self.__routes.add(route)

    def delete_route(self, index: int):
        self.__routes.remove(index)
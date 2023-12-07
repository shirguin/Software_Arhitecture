from datetime import datetime


class Ticket:
    def __init__(self, id: int, price: float, date_time: datetime, is_valid: bool):
        self.__id = id
        self.__price = price
        self.__date_time = date_time
        self.__is_valid = is_valid

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_date_time(self):
        return self.__date_time

    def set_date_time(self, date_time):
        self.__date_time = date_time

    def set_is_valid(self):
        return self.__is_valid

    def get_is_valid(self, is_valid):
        self.__is_valid = is_valid

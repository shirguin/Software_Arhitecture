from BankAccount import BankAccount


class User:
    def __init__(self, id: int, user_name: str, hash_password: int, account: BankAccount):
        self.__id = id
        self.__user_name = user_name
        self.__hash_password = hash_password
        self.__account = account

    def set_id(self):
        return self.__id

    def get_id(self, id):
        self.__id = id

    def set_user_name(self):
        return self.__user_name

    def get_id(self, user_name):
        self.__user_name = user_name

    def set_password(self):
        return self.__hash_password

    def get_password(self, password):
        self.__hash_password = password

    def get_account(self):
        return self.__account

    def set_is_valid(self, account):
        self.__account = account
class BankAccount:
    def __init__(self, cart_number, balance):
        self.__cart_number = cart_number
        self.__balance = balance

    def set_cart_number(self, cart_number):
        if type(cart_number) in (int, float):
            self.__cart_number = cart_number
        else:
            raise ValueError("данные должны быть числами")

    def get_cart_number(self):
        return self.__cart_number

    def set_balance(self, balance):
        if type(balance) in (int, float):
            self.__balance = balance
        else:
            raise ValueError("данные должны быть числами")

    def get_balance(self):
        return self.__balance


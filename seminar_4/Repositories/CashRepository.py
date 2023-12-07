from  Data.BankAccount import BankAccount


class Cash_repository:
    account = BankAccount
    def __init__(self, accounts: BankAccount):
        self.__accounts = accounts

    def cash_repository(self):
        self.__accounts = []

    def get_account(self, cart_number):
        for self.account in self.__accounts:
            if self.account.get_cart_number() == cart_number:
                return
        return None

    def set_account(self, account):
        self.__accounts.add(account)

    def delete_account(self, cart_number):
        self.__accounts.get_cart_number() == cart_number
        self.__accounts.remove(cart_number)
        # for (int i = 0; i < self.accounts.size(); i++)
        #     if (self.accounts.get(i).get_cart_number() == cart_number)
        #         self.accounts.remove(i)
        #         break;

    def get_accounts(self):
        return self.__accounts

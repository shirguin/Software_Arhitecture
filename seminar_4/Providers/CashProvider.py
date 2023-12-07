from Data.BankAccount import BankAccount
from Data.Repositories import CashRepository


class CashProvider:
    cash_repository = CashRepository

    def cash_provider(self, cash_repository):
        self.cash_repository = cash_repository

    def create_account(self, card_number, balance):
        account = BankAccount(card_number, balance)
        self.cash_repository.set_account(account)

    def update_account(self, card_number, balance):
        account = BankAccount(self.cash_repository.get_accounts())
        account.get_cart_number = card_number
        account.set_balance(balance)
        return None

    def delete_account(self, card_number):
        self.cash_repository.delete_account(card_number)

    def read_account(self, card_number):
        return self.cash_repository.get_account(card_number)
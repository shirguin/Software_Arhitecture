from Data.BankAccount import BankAccount
from Data.User import User
from Repositories.UserRepository import UserRepository


class UserProvider:
    user_repository = UserRepository

    def user_provider(self):
        self.user_repository = UserRepository()

    def create_user(self,  user_name, hash_password, account: BankAccount):
        user = User(self.user_repository.get_users().size() + 1, user_name, hash_password, account)
        self.user_repository.set_user(user)

    def update_user(self, index, user_name):
        self.user_repository.get_user(index).set_user_name(user_name)

    def delete_user(self, index):
        self.user_repository.delete_user(index)

    def read_user(self, index):
        self.user_repository.get_user(index)
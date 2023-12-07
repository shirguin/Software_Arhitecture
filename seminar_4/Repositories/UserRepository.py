from Data.User import User


class UserRepository:
    def __init__(self, users: User):
        self.__users = users

    def user_repository(self):
        self.__users = list

    def get_user(self, index):
        return self.__users.get(index)

    def set_user(self,  user):
        self.__users.add(user)

    def delete_user(self, index):
        self.__users.remove(index)

    def get_users(self):
        return self.__users

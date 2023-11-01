from GameManager.BetManager import BetManager


class Player:

    def __init__(self, id_user, username):
        if id_user < 0:
            self.__id = id_user
            self.__username = username
            self.__balance = 1000
        else:
            pass
        self.bet_manager: BetManager = BetManager()

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def change_username(self, new_username):
        self.__username = new_username

    def add_balance(self, money):
        self.__balance += money

    def get_data(self):
        pass

    def charge_card(self):
        pass

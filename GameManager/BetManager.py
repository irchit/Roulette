from Domain import Player
from Domain.Number import Number
from Domain.Selection import Selection

MIN_BET_SELECTION: float = 0.5
MIN_BET_NUMBER: float = 0.1


class BetManager:

    def __init__(self):
        self.__bet_selection = MIN_BET_SELECTION
        self.__bet_number = MIN_BET_NUMBER
        self.__bets = {}

    def raise_bet(self, new_bet: float):
        self.__bet_number = new_bet
        if new_bet < MIN_BET_SELECTION:
            self.__bet_selection = MIN_BET_SELECTION
        else:
            self.__bet_selection = new_bet

    def place_bet_number(self, number: Number):
        if number not in self.__bets:
            self.__bets[number] = 0
        self.__bets[number] += self.__bet_number

    def place_bet_selection(self, selection: Selection):
        if selection not in self.__bets:
            self.__bets[selection] = 0
        self.__bets[selection] += self.__bet_selection

    def clear_bets(self):
        self.__bets = []

    def get_bets(self):
        return self.__bets

    def validate_bet(self, user_input):
        pass

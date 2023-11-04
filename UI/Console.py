import random
import time

from Domain.Player import Player
from Errors.TimeoutException import TimeoutException
from GameManager.Game import Game
from GameManager.TimedFunction import TimedFunction


class Console:

    def __init__(self, player: Player):
        self.__game = Game(1, player)
        self.__history = ["History: "]
        self.__number_list = [0, 32, 15, 19, 4, 21, 2,
                              25, 17, 34, 6, 27, 13, 36,
                              11, 30, 8, 23, 10, 5, 24, 16,
                              33, 1, 20, 14, 31, 9, 22, 18,
                              29, 7, 28, 12, 35, 3, 26]
        self.__table = [
            ["____________________________________________"],
            ["|  ", "|   col1   |     col2    |     col3    |________"],
            ["|  ", "|", "3", "6", "9", "12", "|", "15", "18", "21", "24", "|", "27", "30", "33", "36", "|", "line1 |"],
            ["| 0", "|", "2", "5", "8", "11", "|", "14", "17", "20", "23", "|", "26", "29", "32", "35", "|", "line2 |"],
            ["|  ", "|", "1", "4", "7", "10", "|", "13", "16", "19", "22", "|", "25", "28", "31", "34", "|", "line3 |"],
            ["|___|__________|_____________|_____________|_______|"],
            ["   ", "|", "1-18", "|", "even", "|", "red", "|", "black", "|", "odd", "|", "19-36 |"],
            ["    |______|______|_____|_______|_____|_______|"]
        ]
        self.__text = "Place bet like: 'red', 'black', 'even', 'odd',\n" \
                      "'line1', 'line2', 'line3', 'col1', 'col2', \n" \
                      "'col3', '1-18', '19-36' or a number, like '24'."

    def __bet_period(self):
        start_time = time.time()
        while time.time() - start_time < 30:
            timed_input = TimedFunction(input, 30 - (time.time() - start_time), "Enter bet: ")
            try:
                user_input = timed_input.run()
            except TimeoutException:
                return
            bet_type = self.__game.player.bet_manager.validate_bet(user_input)
            if bet_type == "number":
                self.__game.player.bet_manager.place_bet_number()
            elif bet_type == "selection":
                self.__game.player.bet_manager.place_bet_selection()

    def runtime(self):
        while True:
            self.__ui()
            num = random.randint(0, 36)
            self.__bet_period()
            self.__roulette_animation(num)

    def __ui(self):
        print("Balance: " + str(self.__game.player.get_balance()) + "$")
        for elem in self.__history:
            print(elem, end=" ")
        print("\n")
        for line in self.__table:
            for col in line:
                print(col, end=" ")
            print("")
        print("\n")
        print(self.__text + "\n\n30 seconds to bet, minimum one bet to spin:\n")

    def __roulette_animation(self, num):
        pass


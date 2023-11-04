from Domain.Color import Color
from Domain.Number import Number
from Domain.Player import Player
from Domain.Selection import Selection
from Errors.GameExecutionError import GameExecutionError


class Game:

    def __init__(self, id_game: int, player: Player):
        self.__id = id_game
        self.player = player
        self.numbers = []
        self.selections = []
        self.__setup()

    def __setup(self):
        reds = []
        blacks = []
        evens = []
        odds = []
        line1 = []
        line2 = []
        line3 = []
        with open("data_roulette.txt", "r") as f:
            line = f.readline()
            number, color = line.split()
            if int(number) % 3 == 0:
                line1.append(int(number))
            elif int(number) % 3 == 1:
                line3.append(int(number))
            elif int(number) % 3 == 2:
                line2.append(int(number))
            if color == "red":
                c = Color.RED
                reds.append(int(number))
            else:
                c = Color.BLACK
                blacks.append(int(number))
            if int(number) % 2 == 0 and int(number) != 0:
                evens.append(int(number))
            else:
                odds.append(int(number))
            self.numbers.append(Number(int(number), c))
        self.selections.append(Selection("odds", odds))
        self.selections.append(Selection("blacks", blacks))
        self.selections.append(Selection("reds", reds))
        self.selections.append(Selection("even", evens))
        self.selections.append(Selection("1st", list(range(1, 13))))
        self.selections.append(Selection("2st", list(range(13, 25))))
        self.selections.append(Selection("3st", list(range(25, 37))))
        self.selections.append(Selection("1-18", list(range(1, 19))))
        self.selections.append(Selection("19-36", list(range(19, 37))))


from Domain import Color


class Number:

    def __init__(self, value: int, color: Color):
        self.__value: int = value
        self.__color: Color = color

    def __hash__(self):
        return f"N{str(self.__value)}"

    def __eq__(self, other):
        return hash(self) == hash(other)

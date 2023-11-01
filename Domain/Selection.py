class Selection:

    def __init__(self, name, list_of_numbers):
        self.__name = name
        self.__list_of_numbers = list_of_numbers

    def __hash__(self):
        return f"S{str(self.__name)}"

    def __eq__(self, other):
        return hash(self) == hash(other)

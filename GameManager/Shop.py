class Shop:

    def __init__(self, player):
        self.__player = player
        self.__products = {
            "1000": 5,
            "10000": 25,
            "100000": 100
        }

    def get_products(self):
        return self.__products

    def buy(self, sum_of_money):
        if str(sum_of_money) not in self.__products:
            raise Exception("Product not found...")
        self.__player.charge_card(self.__products[sum_of_money])
        self.__player.add_money(sum_of_money)


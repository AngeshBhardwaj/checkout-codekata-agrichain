from utils.helper import *


class OfferList:

    def __init__(self) -> None:
        self._offers = {}

    def add_offer(self, item, quantity, price):
        if len(item) > 1:
            raise ValueError('Item name must have 1 character only')

        # check if the offer has an entry for item already? If not, add it to prevent KeyError
        if item not in self._offers:
                    self._offers[item] = {}
        self._offers[item][quantity] = price
    
    @property
    def offers(self):
        return self._offers.items()
    
    
# offers_data = get_csv_data_from_file('offers.csv')

available_offers = OfferList()
available_offers.add_offer('A', 3, 130)
available_offers.add_offer('B', 2, 45)
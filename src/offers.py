from utils.helper import *
from utils.logger import logger


class OfferList:

    def __init__(self) -> None:
        self._offers = {}

    def add_offer(self, item, quantity, price):
        """
        The function `add_offer` adds a new offer for an item with a specified quantity and price to a
        dictionary of offers.
        
        :param item: The `item` parameter in the `add_offer` method represents the name of the item for
        which you are adding an offer
        :param quantity: The `quantity` parameter in the `add_offer` method represents the number of
        items being offered at a specific price. It indicates how many units of the item are available
        at the given price in the offer
        :param price: The `price` parameter in the `add_offer` method represents the cost of the item
        for the specified quantity in the offer. It is the amount that the customer would need to pay
        for purchasing the specified quantity of the item
        """
        if len(item) > 1:
            logger.error('Item name must have 1 character only')
            raise ValueError('Item name must have 1 character only')

        # check if the offer has an entry for item already? If not, add it to prevent KeyError
        if item not in self._offers:
                    self._offers[item] = {}
        self._offers[item][quantity] = price
    
    @property
    def offers(self):
        """
        The function "offers" returns a view object of the key-value pairs in the "_offers" attribute of
        the object.
        :return: The `offers` method is returning the items of the `_offers` dictionary as a list of
        tuples. Each tuple contains a key-value pair from the dictionary.
        """
        return self._offers.items()
    
## To-DO   
# offers_data = get_csv_data_from_file('offers.csv')

# creates an instance of the `OfferList` class,
# initializing an object named `available_offers` that will store offers for items.
available_offers = OfferList()
available_offers.add_offer('A', 3, 130)
available_offers.add_offer('B', 2, 45)
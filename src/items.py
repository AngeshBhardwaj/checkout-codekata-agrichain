from utils.helper import *


class ItemList:

    def __init__(self) -> None:
        self._items = {}

    def add_item(self, item, price):
        """
        The function `add_item` adds an item with its price to a dictionary, but raises a ValueError if
        the item name has more than 1 character.
        
        :param item: The `item` parameter in the `add_item` method is the name of the item that you want
        to add to the collection
        :param price: The `price` parameter in the `add_item` method represents the cost or price
        associated with the item being added to the collection. It is used to store the price of the
        item in the `_items` dictionary, where the item name serves as the key and the price serves as
        the value
        """
        if len(item) > 1:
            raise ValueError('Item name must have 1 character only')

        self._items[item] = price
    
    @property
    def items(self):
        """
        This function returns the items of a dictionary-like object.
        :return: The `items` method is returning a view object that displays a list of a dictionary's
        key-value pairs.
        """
        return self._items.items()
    
## To-DO
# items_data = get_csv_data_from_file('items.csv')

# Create an instance of the `ItemList` class named `available_items` and adding
# items with their prices to the `_items` dictionary within the `ItemList` class.
available_items = ItemList()
available_items.add_item('A', 50)
available_items.add_item('B', 30)
available_items.add_item('C', 20)
available_items.add_item('D', 15)
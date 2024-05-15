from utils.helper import *


class ItemList:

    def __init__(self) -> None:
        self._items = {}

    def add_item(self, item, price):
        if len(item) > 1:
            raise ValueError('Item name must have 1 character only')

        self._items[item] = price
    
    @property
    def items(self):
        return self._items.items()
    

# items_data = get_csv_data_from_file('items.csv')

available_items = ItemList()
available_items.add_item('A', 50)
available_items.add_item('B', 30)
available_items.add_item('C', 20)
available_items.add_item('D', 15)
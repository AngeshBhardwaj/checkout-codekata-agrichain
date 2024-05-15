from src.items import available_items
from src.offers import available_offers

class Checkout:
    cart_items = ''

    def scan(self, item):
        self.cart_items += item

    @property
    def price(self):
        self.cart_items = ''.join(sorted(self.cart_items))
        return self._compute_price(available_items.items, available_offers.offers)

    def _compute_price(self, items, offers):
        price = 0

        ## Revisit this and see if the for loops can be reduced. e.g. by fetching details using key and just looping through cart items.
        # Iterate through items list to find if the item exists in cart
        for item, item_price in items:
            if item in self.cart_items:
                offer_applied = False
                #Iterate through offers to see if there is any offer on the current item
                for offer_item, quantity in offers:
                    if offer_item == item:
                        # Build a pattern to check offer eligiblity. Say if the offer is on 2 'A' items, the pattern will be 'AA'.
                        for q, p in quantity.items():
                            item_pattern = item * q
                            # if the pattern exists in cart, offer can be applied!
                            # Add the offer price for all the pattern count in cart and remove the cart items once processed.
                            if item_pattern in self.cart_items:
                                offer_applied = True
                                price += p *  self.cart_items.count(item_pattern)
                                self.cart_items = self.cart_items.replace(item_pattern, '')
                
                # If offer was not applied or partially applied (i.e. there are more items than the offer)
                # Add the price for all the item count in cart and remove the cart items once processed.
                if not offer_applied or (offer_applied and item in self.cart_items):
                    price += item_price * self.cart_items.count(item)
                    self.cart_items = self.cart_items.replace(item, '')
                        
        return price


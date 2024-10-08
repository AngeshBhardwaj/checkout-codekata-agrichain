import time
from src.checkout import Checkout
from src.items import available_items
from src.offers import available_offers
from utils.logger import logger


def print_welcome_menu():
    """
    The function `print_welcome_menu` displays a welcome message and the pricing information for
    available items with special offers.
    """
    print("\n*********************************\n Hey There! Welcome to the Shop.\n*********************************")
    print("\nProduct pricing for this week is as below:\n")
    print("\nItem\tUnit price\tSpecial Price\n------------------------------------------------")
    for item, price in available_items.items:
        offer_text = ''
        for offer_item, offer in available_offers.offers:
            if offer_item == item:
                for q, p in offer.items():
                    offer_text = '{0} for {1}'.format(q, p)
                break
        print('  {0}\t    {1}\t\t  {2}'.format(item, price, offer_text))


def get_valid_menu_selection(sel_option: str):
    """
    The function `get_valid_menu_selection` converts a given string input to an integer, returning 0 if
    the conversion fails.
    
    :param sel_option: The function `get_valid_menu_selection` takes a string input `sel_option` and
    attempts to convert it into an integer. If the conversion is successful, it returns the integer
    value. If there is an exception during the conversion (e.g., if the input is not a valid integer),
    it returns
    :return: The function `get_valid_menu_selection` returns the valid menu selection option as an
    integer. If the input `sel_option` can be converted to an integer successfully, it returns that
    integer value. If the conversion fails (e.g., if the input is not a valid integer), it returns 0.
    """
    valid_sel_option = 0
    try:
        valid_sel_option = int(sel_option)
    except:
        logger.warning("Invalid option selected: {}".format(sel_option))
        valid_sel_option = 0
    
    return valid_sel_option


if __name__ == '__main__':

    # print the welcome message and sales info
    print_welcome_menu()
    
    # print the interactive Menu to gauge action and perform it accordingly
    time.sleep(1)
    print("\nWhat would you like to do? Please select an option:\n\t1. Scan items for checkout.\n\t2. Exit the application.")
    main_menu_sel = 0
    while main_menu_sel != 1 or main_menu_sel != 2:
        main_menu_sel = get_valid_menu_selection(input())
        logger.info("Main menu option selected: {}".format(main_menu_sel))

        if main_menu_sel == 2:
            logger.info("Confirming if the user wants to exit?")
            print("\nAre you sure you want to exit?. Enter Y to confirm.")
            exit_cnf = input()
            if exit_cnf.upper() == 'Y':
                logger.warning("Exit confirmed by user. Exiting...")
                exit(0)
            else:
                main_menu_sel = 0
                print("\nYou have been switched back to the main menu. Please select an option:\n\t1. Scan items for checkout.\n\t2. Exit the application.")
            
        elif main_menu_sel == 1:
            action_menu_sel = 0
            shopping_cart = Checkout()

            while action_menu_sel != 2:
                print("\nWhat would you like to do with your shopping cart?\n\t1. Scan an item and add it.\n\t2. Calculate the total amount and check-out.")
                action_menu_sel = get_valid_menu_selection(input())
                logger.info("Action menu option selected: {}".format(action_menu_sel))

                if action_menu_sel == 1:
                    new_cart_item = input()
                    shopping_cart.scan(new_cart_item)
                    print("The item has been added to your cart! Items in cart are: {}".format(shopping_cart.cart_items))
                elif action_menu_sel == 2:
                    final_cart = shopping_cart.cart_items
                    total_price = shopping_cart.price
                    print("\nThe total price of items in your cart is: {}\nThanks for Shopping!".format(total_price))
                    logger.info("Cart checked out successfully. Cart Items: '{}', Cart total price: {}".format(final_cart, total_price))
                else:
                    print("You have selected an invalid option, please select a valid option.")
            
            # set the user back to main menu so he can use the app again.
            time.sleep(1)
            logger.info("Action menu options completed, switching the user back to 'Main menu'.")
            print("\nPlease select an option:\n\t1. Scan items for checkout.\n\t2. Exit the application.")
        else:
            print("You have selected an invalid option, please select a valid option.")
    

    # shopping_cart = Checkout()
    # shopping_cart.scan('A')
    # shopping_cart.scan('B')

    # total_price = shopping_cart.price
    # print(total_price)